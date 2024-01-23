"""Test MosaicML API wrapper."""
import re

import pytest

from langchain_community.llms.mosaicml import PROMPT_FOR_GENERATION_FORMAT, MosaicML


def test_mosaicml_llm_call() -> None:
    """Test valid call to MosaicML."""
    llm = MosaicML(model_kwargs={})
    output = llm("Say foo:")
    assert isinstance(output, str)


def test_mosaicml_endpoint_change() -> None:
    """Test valid call to MosaicML."""
    new_url = "https://models.hosted-on.mosaicml.hosting/mpt-30b-instruct/v1/predict"
    llm = MosaicML(endpoint_url=new_url)
    assert llm.endpoint_url == new_url
    output = llm("Say foo:")
    assert isinstance(output, str)


def test_mosaicml_extra_kwargs() -> None:
    llm = MosaicML(model_kwargs={"max_new_tokens": 1})
    assert llm.model_kwargs == {"max_new_tokens": 1}

    output = llm("Say foo:")

    assert isinstance(output, str)

    # should only generate one new token (which might be a new line or whitespace token)
    assert len(output.split()) <= 1


def test_instruct_prompt() -> None:
    """Test instruct prompt."""
    llm = MosaicML(inject_instruction_format=True, model_kwargs={"max_new_tokens": 10})
    instruction = "Repeat the word foo"
    prompt = llm._transform_prompt(instruction)
    expected_prompt = PROMPT_FOR_GENERATION_FORMAT.format(instruction=instruction)
    assert prompt == expected_prompt
    output = llm(prompt)
    assert isinstance(output, str)


def test_retry_logic() -> None:
    """Tests that two queries (which would usually exceed the rate limit) works"""
    llm = MosaicML(inject_instruction_format=True, model_kwargs={"max_new_tokens": 10})
    instruction = "Repeat the word foo"
    prompt = llm._transform_prompt(instruction)
    expected_prompt = PROMPT_FOR_GENERATION_FORMAT.format(instruction=instruction)
    assert prompt == expected_prompt
    output = llm(prompt)
    assert isinstance(output, str)
    output = llm(prompt)
    assert isinstance(output, str)


def test_short_retry_does_not_loop() -> None:
    """Tests that two queries with a short retry sleep does not infinite loop"""
    llm = MosaicML(
        inject_instruction_format=True,
        model_kwargs={"do_sample": False},
        retry_sleep=0.1,
    )
    instruction = "Repeat the word foo"
    prompt = llm._transform_prompt(instruction)
    expected_prompt = PROMPT_FOR_GENERATION_FORMAT.format(instruction=instruction)
    assert prompt == expected_prompt

    with pytest.raises(
        ValueError,
        match=re.escape(
            "Error raised by inference API: rate limit exceeded.\nResponse: You have "
            "reached maximum request limit.\n"
        ),
    ):
        for _ in range(10):
            output = llm(prompt)
            assert isinstance(output, str)
