import logging
import os

from langchain import FAISS
from langchain.embeddings import OpenAIEmbeddings
from openai.error import InvalidRequestError, RateLimitError, ServiceUnavailableError, TryAgain
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_random_exponential

from genia.agents.open_ai import OpenAIToolsEmpoweredAgent
from genia.conversation.llm_conversation import LLMConversation, LLMConversationService
from genia.conversation.llm_conversation_in_memory_repository import LLMConversationInMemRepository
from genia.llm_function.llm_function_repository import LLMFunctionRepository
from genia.llm_function.llm_functions_factory import LLMFunctionFactory
from genia.llm_function_lookup_strategy.llm_function_lookup_strategy import (
    LLMFunctionLookupStrategy,
    LLMFunctionLookupStrategyPrevCallsLastUserAndChat,
)
from genia.settings_loader import settings
from genia.token_limiter.token_limiter_openai import TokenLimiter, TokenLimiterOpenAI
from genia.tool_validators.llm_tool_validator import LLMToolValidator
from genia.utils.utils import safe_loads


class OpenAIChat(OpenAIToolsEmpoweredAgent):
    logger = logging.getLogger(__name__)

    _llm_functions_repository: LLMFunctionRepository
    _llm_function_factory: LLMFunctionFactory
    _llm_conversation_service: LLMConversationService
    _llm_tools_validator: LLMToolValidator
    _llm_token_limiter: TokenLimiter
    _function_lookup_strategy: LLMFunctionLookupStrategy

    def __init__(
        self,
        model=settings["openai"]["OPENAI_MODEL"],
        llm_functions_repository=LLMFunctionRepository(
            OpenAIEmbeddings(
                chunk_size=16
                if os.getenv("OPENAI_API_TYPE") == "azure"
                else 1000,  # 1000 is the default also in OpenAIEmbeddings, and 16 in Azure limit
            ),
            FAISS,
        ),
        llm_function_factory=LLMFunctionFactory(OpenAIToolsEmpoweredAgent()),
        llm_conversation_service=LLMConversationService(LLMConversationInMemRepository()),
        llm_tools_validator=LLMToolValidator(),
        llm_token_limiter=TokenLimiterOpenAI(),
        function_lookup_strategy: LLMFunctionLookupStrategy = None,
    ):
        super().__init__(model)
        self._llm_function_factory = llm_function_factory
        self._llm_functions_repository = llm_functions_repository
        self._llm_conversation_service = llm_conversation_service
        self._llm_tools_validator = llm_tools_validator
        self._llm_token_limiter = llm_token_limiter
        if function_lookup_strategy is None:
            function_lookup_strategy = LLMFunctionLookupStrategyPrevCallsLastUserAndChat(
                llm_conversation_service, llm_functions_repository
            )
        self._function_lookup_strategy = function_lookup_strategy

    def process_message(self, current_user_message, uid=0, **kwargs):
        llm_conversation = self._llm_conversation_service.find_conversation_by_id(uid)
        try:
            self._llm_conversation_service.add_user_message(llm_conversation, current_user_message)

            # run a chain of function calls as determined by the model with a limited length
            for _ in range(settings["chat"]["max_function_chain_length"]):
                response = self.execute_model_request(llm_conversation)
                message = response["choices"][0]["message"]
                finish_reason = response["choices"][0]["finish_reason"]

                if finish_reason == "stop":
                    self._llm_conversation_service.add_assistant_message(llm_conversation, message["content"])
                    return message["content"]

                elif finish_reason == "function_call":
                    function_name = message["function_call"]["name"]
                    function_arguments = safe_loads(message["function_call"]["arguments"])
                    self.logger.debug(
                        "the model decided to call the function: %s, with parameters: %s",
                        function_name,
                        function_arguments,
                    )
                    try:
                        llm_matching_tool = self._llm_functions_repository.find_tool_by_name(function_name)
                        if llm_matching_tool is None:
                            raise ValueError("function {} doesn't exist".format(llm_matching_tool))
                        self.logger.debug("found the tool: %s", llm_matching_tool)
                        if self._llm_tools_validator.is_tool_validation_required(
                            self._llm_conversation_service,
                            self._llm_functions_repository,
                            llm_matching_tool,
                            function_arguments,
                            llm_conversation,
                        ):
                            return self._llm_tools_validator.validate_tool_usage(
                                self._llm_conversation_service,
                                llm_conversation,
                                function_arguments,
                                llm_matching_tool,
                            )
                        else:
                            function_response = self._llm_function_call(
                                llm_conversation,
                                function_name,
                                function_arguments,
                                llm_matching_tool,
                            )
                    except Exception as e:
                        function_response = str(e)
                        self.logger.exception(
                            "Error executing function=%s, parameters=%s, error=%s",
                            function_name,
                            function_arguments,
                            function_response,
                        )

                    self.logger.debug("function response: %s", function_response)
                    self._llm_conversation_service.add_function_response_message(
                        llm_conversation, function_name, function_response
                    )

            self.logger.critical(
                "function chain length exceeded max allowed %d",
                settings["chat"]["max_function_chain_length"],
            )
        except Exception as e:
            self.logger.exception("exception occured during chat message execution %s", str(e))
        finally:
            self._llm_conversation_service.pretty_print_conversation(llm_conversation, self.logger)
            self._llm_conversation_service.persist(llm_conversation)
        return settings["agent_prompt"]["error_message"]

    @retry(
        wait=wait_random_exponential(multiplier=0.5, max=30),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type((RateLimitError, ServiceUnavailableError)),
    )
    def execute_model_request(self, llm_conversation: LLMConversation):
        try:
            functions = self._function_lookup_strategy.find_potential_tools(llm_conversation)
            messages = self._llm_conversation_service.build_messages_for_model(llm_conversation)
            if self._llm_token_limiter.has_limit_reached(self._model, messages, functions):
                self._llm_conversation_service.handle_context_too_long(llm_conversation)
            response = self.call_model(messages, functions, settings["openai"].get("function_call", "auto"))
            self.logger.debug("Tokens usage recorded by open AI %s", response["usage"]["total_tokens"])
            self.logger.debug("LLM call took %s ms", str(response.response_ms))
            return response
        except Exception as e:
            self.logger.exception("exception occured during execute model request %s", str(e))
            if type(e) == InvalidRequestError and "maximum context length" in str(e):
                self.logger.warning("maximum context length by open AI %s", str(e))
                self._llm_conversation_service.handle_context_too_long(llm_conversation)
                raise TryAgain
            raise e

    def _llm_function_call(self, llm_conversation: LLMConversation, function_name, function_arguments, llm_matching_tool):
        self.logger.debug("Invoking: '%s' with the arguments: %s", function_name, function_arguments)
        self._llm_conversation_service.add_assistant_function_call_message(
            llm_conversation, function_name, function_arguments
        )
        llm_function = self._llm_function_factory.create_function(
            llm_matching_tool.get("category"),
            self._llm_functions_repository,
            llm_conversation,
            self._function_lookup_strategy,
        )
        function_response = str(llm_function.evaluate(llm_matching_tool, function_arguments))
        return self._llm_token_limiter.limit_function_response_tokens(function_response)
