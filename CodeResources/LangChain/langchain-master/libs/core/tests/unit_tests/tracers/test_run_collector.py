"""Test the run collector."""

import uuid

from langchain_core.tracers.context import collect_runs
from tests.unit_tests.fake.llm import FakeListLLM


def test_collect_runs() -> None:
    llm = FakeListLLM(responses=["hello"])
    with collect_runs() as cb:
        llm.predict("hi")
        assert cb.traced_runs
        assert len(cb.traced_runs) == 1
        assert isinstance(cb.traced_runs[0].id, uuid.UUID)
        assert cb.traced_runs[0].inputs == {"prompts": ["hi"]}
