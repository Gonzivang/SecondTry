import logging
import time
import uuid

import streamlit as st

from genia.agents.chat import OpenAIChat
from genia.settings_loader import settings

oa = OpenAIChat()


class StreamlitApp:
    logger = logging.getLogger(__name__)

    def __init__(self):

        genia_examples = [
            "List some of the tools you have",
            "List your k8s tools",
            "Summarize the following github PR 'https://github.com/openai/triton/pull/1848'",
        ]

        grayed_out_examples = [
            "What AWS lambda functions are running on us-east-1?",
            "Generate a report detailing unutilized cloud resources per team and share it on Slack",
            "Conduct a security vulnerability analysis on your S3 buckets",
            "why did my last argo deploy failed?",
            "grant the user 'shlomsh' production permissions",
            "find unlabled EC2 instances",
        ]

        st.set_page_config(
            page_title="GeniA Your Engineering GenAI Assistant",
            page_icon="🧬🤖💻",
            # layout="wide",
            initial_sidebar_state='collapsed',
            menu_items={"About": "https://www.genia.dev"},
        )

        st.title("GeniA")
        st.text("Your Engineering GenAI Assistant 🧬🤖💻")

        with st.sidebar:
            st.header("Check out some of the use cases GeniA can help you with:")
            for example in genia_examples:
                st.markdown("- " + example)
            st.divider()
            st.caption("Note: Genia is crafted for team collaboration and works best in slack")
            with st.expander("Additional prompts", expanded=False):
                st.caption("set your credentials to try these:")
                for example in grayed_out_examples:
                    st.markdown("<span style='opacity: 0.5;'>" + example + "<span>", unsafe_allow_html=True)

        # Initialize chat conversation
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from conversation on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html=True)

        # Accept user input
        if prompt := st.chat_input("Hi, How can i assist you today?"):
            # Add user message to chat conversation
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt, unsafe_allow_html=True)

            with st.chat_message("assistant"):
                with st.spinner(settings.slack.wait_message):
                    message_placeholder = st.empty()
                    full_response = ""
                    if "session_id" not in st.session_state:
                        st.session_state["session_id"] = str(uuid.uuid4())

                    self.logger.debug(f"session state: {st.session_state}")
                    assistant_response = oa.process_message(prompt, st.session_state.session_id)

                    # Replace \n with <br> in the assistant response
                    assistant_response = assistant_response.replace("\n", "</br>")

                # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)
                message_placeholder.markdown(full_response, unsafe_allow_html=True)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

            st.markdown(
                """
                    <style>
                        .sidebar .sidebar-content {{
                            width: 375px;
                        }}
                    </style>
                """,
                unsafe_allow_html=True,
            )
