"""Test LLM saving and loading functions."""
from pathlib import Path
from unittest.mock import patch

from langchain_community.llms.loading import load_llm
from tests.unit_tests.llms.fake_llm import FakeLLM


@patch(
    "langchain_community.llms.loading.get_type_to_cls_dict",
    lambda: {"fake": lambda: FakeLLM},
)
def test_saving_loading_round_trip(tmp_path: Path) -> None:
    """Test saving/loading a Fake LLM."""
    fake_llm = FakeLLM()
    fake_llm.save(file_path=tmp_path / "fake_llm.yaml")
    loaded_llm = load_llm(tmp_path / "fake_llm.yaml")
    assert loaded_llm == fake_llm
