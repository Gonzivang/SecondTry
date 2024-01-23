"""Test Redis cache functionality."""
import uuid
from typing import List, cast

import pytest
from langchain_core.embeddings import Embeddings
from langchain_core.load.dump import dumps
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.outputs import ChatGeneration, Generation, LLMResult

from langchain.cache import RedisCache, RedisSemanticCache
from langchain.globals import get_llm_cache, set_llm_cache
from tests.integration_tests.cache.fake_embeddings import (
    ConsistentFakeEmbeddings,
    FakeEmbeddings,
)
from tests.unit_tests.llms.fake_chat_model import FakeChatModel
from tests.unit_tests.llms.fake_llm import FakeLLM

REDIS_TEST_URL = "redis://localhost:6379"


def random_string() -> str:
    return str(uuid.uuid4())


def test_redis_cache_ttl() -> None:
    import redis

    set_llm_cache(RedisCache(redis_=redis.Redis.from_url(REDIS_TEST_URL), ttl=1))
    llm_cache = cast(RedisCache, get_llm_cache())
    llm_cache.update("foo", "bar", [Generation(text="fizz")])
    key = llm_cache._key("foo", "bar")
    assert llm_cache.redis.pttl(key) > 0


def test_redis_cache() -> None:
    import redis

    set_llm_cache(RedisCache(redis_=redis.Redis.from_url(REDIS_TEST_URL)))
    llm = FakeLLM()
    params = llm.dict()
    params["stop"] = None
    llm_string = str(sorted([(k, v) for k, v in params.items()]))
    get_llm_cache().update("foo", llm_string, [Generation(text="fizz")])
    output = llm.generate(["foo"])
    expected_output = LLMResult(
        generations=[[Generation(text="fizz")]],
        llm_output={},
    )
    assert output == expected_output
    llm_cache = cast(RedisCache, get_llm_cache())
    llm_cache.redis.flushall()


def test_redis_cache_chat() -> None:
    import redis

    set_llm_cache(RedisCache(redis_=redis.Redis.from_url(REDIS_TEST_URL)))
    llm = FakeChatModel()
    params = llm.dict()
    params["stop"] = None
    llm_string = str(sorted([(k, v) for k, v in params.items()]))
    prompt: List[BaseMessage] = [HumanMessage(content="foo")]
    get_llm_cache().update(
        dumps(prompt), llm_string, [ChatGeneration(message=AIMessage(content="fizz"))]
    )
    output = llm.generate([prompt])
    expected_output = LLMResult(
        generations=[[ChatGeneration(message=AIMessage(content="fizz"))]],
        llm_output={},
    )
    assert output == expected_output
    llm_cache = cast(RedisCache, get_llm_cache())
    llm_cache.redis.flushall()


def test_redis_semantic_cache() -> None:
    set_llm_cache(
        RedisSemanticCache(
            embedding=FakeEmbeddings(), redis_url=REDIS_TEST_URL, score_threshold=0.1
        )
    )
    llm = FakeLLM()
    params = llm.dict()
    params["stop"] = None
    llm_string = str(sorted([(k, v) for k, v in params.items()]))
    get_llm_cache().update("foo", llm_string, [Generation(text="fizz")])
    output = llm.generate(
        ["bar"]
    )  # foo and bar will have the same embedding produced by FakeEmbeddings
    expected_output = LLMResult(
        generations=[[Generation(text="fizz")]],
        llm_output={},
    )
    assert output == expected_output
    # clear the cache
    get_llm_cache().clear(llm_string=llm_string)
    output = llm.generate(
        ["bar"]
    )  # foo and bar will have the same embedding produced by FakeEmbeddings
    # expect different output now without cached result
    assert output != expected_output
    get_llm_cache().clear(llm_string=llm_string)


def test_redis_semantic_cache_multi() -> None:
    set_llm_cache(
        RedisSemanticCache(
            embedding=FakeEmbeddings(), redis_url=REDIS_TEST_URL, score_threshold=0.1
        )
    )
    llm = FakeLLM()
    params = llm.dict()
    params["stop"] = None
    llm_string = str(sorted([(k, v) for k, v in params.items()]))
    get_llm_cache().update(
        "foo", llm_string, [Generation(text="fizz"), Generation(text="Buzz")]
    )
    output = llm.generate(
        ["bar"]
    )  # foo and bar will have the same embedding produced by FakeEmbeddings
    expected_output = LLMResult(
        generations=[[Generation(text="fizz"), Generation(text="Buzz")]],
        llm_output={},
    )
    assert output == expected_output
    # clear the cache
    get_llm_cache().clear(llm_string=llm_string)


def test_redis_semantic_cache_chat() -> None:
    set_llm_cache(
        RedisSemanticCache(
            embedding=FakeEmbeddings(), redis_url=REDIS_TEST_URL, score_threshold=0.1
        )
    )
    llm = FakeChatModel()
    params = llm.dict()
    params["stop"] = None
    llm_string = str(sorted([(k, v) for k, v in params.items()]))
    prompt: List[BaseMessage] = [HumanMessage(content="foo")]
    get_llm_cache().update(
        dumps(prompt), llm_string, [ChatGeneration(message=AIMessage(content="fizz"))]
    )
    output = llm.generate([prompt])
    expected_output = LLMResult(
        generations=[[ChatGeneration(message=AIMessage(content="fizz"))]],
        llm_output={},
    )
    assert output == expected_output
    get_llm_cache().clear(llm_string=llm_string)


@pytest.mark.parametrize("embedding", [ConsistentFakeEmbeddings()])
@pytest.mark.parametrize(
    "prompts,  generations",
    [
        # Single prompt, single generation
        ([random_string()], [[random_string()]]),
        # Single prompt, multiple generations
        ([random_string()], [[random_string(), random_string()]]),
        # Single prompt, multiple generations
        ([random_string()], [[random_string(), random_string(), random_string()]]),
        # Multiple prompts, multiple generations
        (
            [random_string(), random_string()],
            [[random_string()], [random_string(), random_string()]],
        ),
    ],
    ids=[
        "single_prompt_single_generation",
        "single_prompt_multiple_generations",
        "single_prompt_multiple_generations",
        "multiple_prompts_multiple_generations",
    ],
)
def test_redis_semantic_cache_hit(
    embedding: Embeddings, prompts: List[str], generations: List[List[str]]
) -> None:
    set_llm_cache(RedisSemanticCache(embedding=embedding, redis_url=REDIS_TEST_URL))

    llm = FakeLLM()
    params = llm.dict()
    params["stop"] = None
    llm_string = str(sorted([(k, v) for k, v in params.items()]))

    llm_generations = [
        [
            Generation(text=generation, generation_info=params)
            for generation in prompt_i_generations
        ]
        for prompt_i_generations in generations
    ]
    for prompt_i, llm_generations_i in zip(prompts, llm_generations):
        print(prompt_i)
        print(llm_generations_i)
        get_llm_cache().update(prompt_i, llm_string, llm_generations_i)
    llm.generate(prompts)
    assert llm.generate(prompts) == LLMResult(
        generations=llm_generations, llm_output={}
    )
