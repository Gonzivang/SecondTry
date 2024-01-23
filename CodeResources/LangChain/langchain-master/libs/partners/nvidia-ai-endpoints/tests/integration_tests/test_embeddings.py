"""Test NVIDIA AI Foundation Model Embeddings.

Note: These tests are designed to validate the functionality of NVIDIAEmbeddings.
"""
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings


def test_nvai_play_embedding_documents() -> None:
    """Test NVIDIA embeddings for documents."""
    documents = ["foo bar"]
    embedding = NVIDIAEmbeddings(model="nvolveqa_40k")
    output = embedding.embed_documents(documents)
    assert len(output) == 1
    assert len(output[0]) == 1024  # Assuming embedding size is 2048


def test_nvai_play_embedding_documents_multiple() -> None:
    """Test NVIDIA embeddings for multiple documents."""
    documents = ["foo bar", "bar foo", "foo"]
    embedding = NVIDIAEmbeddings(model="nvolveqa_40k")
    output = embedding.embed_documents(documents)
    assert len(output) == 3
    assert all(len(doc) == 1024 for doc in output)


def test_nvai_play_embedding_query() -> None:
    """Test NVIDIA embeddings for a single query."""
    query = "foo bar"
    embedding = NVIDIAEmbeddings(model="nvolveqa_40k")
    output = embedding.embed_query(query)
    assert len(output) == 1024


async def test_nvai_play_embedding_async_query() -> None:
    """Test NVIDIA async embeddings for a single query."""
    query = "foo bar"
    embedding = NVIDIAEmbeddings(model="nvolveqa_40k")
    output = await embedding.aembed_query(query)
    assert len(output) == 1024


async def test_nvai_play_embedding_async_documents() -> None:
    """Test NVIDIA async embeddings for multiple documents."""
    documents = ["foo bar", "bar foo", "foo"]
    embedding = NVIDIAEmbeddings(model="nvolveqa_40k")
    output = await embedding.aembed_documents(documents)
    assert len(output) == 3
    assert all(len(doc) == 1024 for doc in output)
