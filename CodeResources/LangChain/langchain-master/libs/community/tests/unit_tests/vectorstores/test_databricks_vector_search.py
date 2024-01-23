import random
import uuid
from typing import List
from unittest.mock import MagicMock

import pytest

from langchain_community.vectorstores import DatabricksVectorSearch
from tests.integration_tests.vectorstores.fake_embeddings import (
    FakeEmbeddings,
    fake_texts,
)

DEFAULT_VECTOR_DIMENSION = 4


class FakeEmbeddingsWithDimension(FakeEmbeddings):
    """Fake embeddings functionality for testing."""

    def __init__(self, dimension: int = DEFAULT_VECTOR_DIMENSION):
        super().__init__()
        self.dimension = dimension

    def embed_documents(self, embedding_texts: List[str]) -> List[List[float]]:
        """Return simple embeddings."""
        return [
            [float(1.0)] * (self.dimension - 1) + [float(i)]
            for i in range(len(embedding_texts))
        ]

    def embed_query(self, text: str) -> List[float]:
        """Return simple embeddings."""
        return [float(1.0)] * (self.dimension - 1) + [float(0.0)]


DEFAULT_EMBEDDING_MODEL = FakeEmbeddingsWithDimension()
DEFAULT_TEXT_COLUMN = "text"
DEFAULT_VECTOR_COLUMN = "text_vector"
DEFAULT_PRIMARY_KEY = "id"

DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS = {
    "name": "ml.llm.index",
    "endpoint_name": "vector_search_endpoint",
    "index_type": "DELTA_SYNC",
    "primary_key": DEFAULT_PRIMARY_KEY,
    "delta_sync_index_spec": {
        "source_table": "ml.llm.source_table",
        "pipeline_type": "CONTINUOUS",
        "embedding_source_columns": [
            {
                "name": DEFAULT_TEXT_COLUMN,
                "embedding_model_endpoint_name": "openai-text-embedding",
            }
        ],
    },
}

DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS = {
    "name": "ml.llm.index",
    "endpoint_name": "vector_search_endpoint",
    "index_type": "DELTA_SYNC",
    "primary_key": DEFAULT_PRIMARY_KEY,
    "delta_sync_index_spec": {
        "source_table": "ml.llm.source_table",
        "pipeline_type": "CONTINUOUS",
        "embedding_vector_columns": [
            {
                "name": DEFAULT_VECTOR_COLUMN,
                "embedding_dimension": DEFAULT_VECTOR_DIMENSION,
            }
        ],
    },
}

DIRECT_ACCESS_INDEX = {
    "name": "ml.llm.index",
    "endpoint_name": "vector_search_endpoint",
    "index_type": "DIRECT_ACCESS",
    "primary_key": DEFAULT_PRIMARY_KEY,
    "direct_access_index_spec": {
        "embedding_vector_columns": [
            {
                "name": DEFAULT_VECTOR_COLUMN,
                "embedding_dimension": DEFAULT_VECTOR_DIMENSION,
            }
        ],
        "schema_json": f"{{"
        f'"{DEFAULT_PRIMARY_KEY}": "int", '
        f'"feat1": "str", '
        f'"feat2": "float", '
        f'"text": "string", '
        f'"{DEFAULT_VECTOR_COLUMN}": "array<float>"'
        f"}}",
    },
}

ALL_INDEXES = [
    DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS,
    DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS,
    DIRECT_ACCESS_INDEX,
]

EXAMPLE_SEARCH_RESPONSE = {
    "manifest": {
        "column_count": 3,
        "columns": [
            {"name": DEFAULT_PRIMARY_KEY},
            {"name": DEFAULT_TEXT_COLUMN},
            {"name": "score"},
        ],
    },
    "result": {
        "row_count": len(fake_texts),
        "data_array": sorted(
            [[str(uuid.uuid4()), s, random.uniform(0, 1)] for s in fake_texts],
            key=lambda x: x[2],  # type: ignore
            reverse=True,
        ),
    },
    "next_page_token": "",
}


def mock_index(index_details: dict) -> MagicMock:
    from databricks.vector_search.client import VectorSearchIndex

    index = MagicMock(spec=VectorSearchIndex)
    index.describe.return_value = index_details
    return index


def default_databricks_vector_search(index: MagicMock) -> DatabricksVectorSearch:
    return DatabricksVectorSearch(
        index,
        embedding=DEFAULT_EMBEDDING_MODEL,
        text_column=DEFAULT_TEXT_COLUMN,
    )


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_init_delta_sync_with_managed_embeddings() -> None:
    index = mock_index(DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS)
    vectorsearch = DatabricksVectorSearch(index)
    assert vectorsearch.index == index


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_init_delta_sync_with_self_managed_embeddings() -> None:
    index = mock_index(DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS)
    vectorsearch = DatabricksVectorSearch(
        index,
        embedding=DEFAULT_EMBEDDING_MODEL,
        text_column=DEFAULT_TEXT_COLUMN,
    )
    assert vectorsearch.index == index


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_init_direct_access_index() -> None:
    index = mock_index(DIRECT_ACCESS_INDEX)
    vectorsearch = DatabricksVectorSearch(
        index,
        embedding=DEFAULT_EMBEDDING_MODEL,
        text_column=DEFAULT_TEXT_COLUMN,
    )
    assert vectorsearch.index == index


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_init_fail_no_index() -> None:
    with pytest.raises(TypeError):
        DatabricksVectorSearch()


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_init_fail_index_none() -> None:
    with pytest.raises(TypeError) as ex:
        DatabricksVectorSearch(None)
    assert "index must be of type VectorSearchIndex." in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_init_fail_text_column_mismatch() -> None:
    index = mock_index(DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS)
    with pytest.raises(ValueError) as ex:
        DatabricksVectorSearch(
            index,
            text_column="some_other_column",
        )
    assert (
        f"text_column 'some_other_column' does not match with the source column of the "
        f"index: '{DEFAULT_TEXT_COLUMN}'." in str(ex.value)
    )


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize(
    "index_details", [DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS, DIRECT_ACCESS_INDEX]
)
def test_init_fail_no_text_column(index_details: dict) -> None:
    index = mock_index(index_details)
    with pytest.raises(ValueError) as ex:
        DatabricksVectorSearch(
            index,
            embedding=DEFAULT_EMBEDDING_MODEL,
        )
    assert "`text_column` is required for this index." in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize("index_details", [DIRECT_ACCESS_INDEX])
def test_init_fail_columns_not_in_schema(index_details: dict) -> None:
    index = mock_index(index_details)
    with pytest.raises(ValueError) as ex:
        DatabricksVectorSearch(
            index,
            embedding=DEFAULT_EMBEDDING_MODEL,
            text_column=DEFAULT_TEXT_COLUMN,
            columns=["some_random_column"],
        )
    assert "column 'some_random_column' is not in the index's schema." in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize(
    "index_details", [DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS, DIRECT_ACCESS_INDEX]
)
def test_init_fail_no_embedding(index_details: dict) -> None:
    index = mock_index(index_details)
    with pytest.raises(ValueError) as ex:
        DatabricksVectorSearch(
            index,
            text_column=DEFAULT_TEXT_COLUMN,
        )
    assert "`embedding` is required for this index." in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize(
    "index_details", [DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS, DIRECT_ACCESS_INDEX]
)
def test_init_fail_embedding_dim_mismatch(index_details: dict) -> None:
    index = mock_index(index_details)
    with pytest.raises(ValueError) as ex:
        DatabricksVectorSearch(
            index,
            text_column=DEFAULT_TEXT_COLUMN,
            embedding=FakeEmbeddingsWithDimension(DEFAULT_VECTOR_DIMENSION + 1),
        )
    assert (
        f"embedding model's dimension '{DEFAULT_VECTOR_DIMENSION + 1}' does not match "
        f"with the index's dimension '{DEFAULT_VECTOR_DIMENSION}'"
    ) in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_from_texts_not_supported() -> None:
    with pytest.raises(NotImplementedError) as ex:
        DatabricksVectorSearch.from_texts(fake_texts, FakeEmbeddings())
    assert (
        "`from_texts` is not supported. "
        "Use `add_texts` to add to existing direct-access index."
    ) in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize(
    "index_details",
    [DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS, DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS],
)
def test_add_texts_not_supported_for_delta_sync_index(index_details: dict) -> None:
    index = mock_index(index_details)
    vectorsearch = default_databricks_vector_search(index)
    with pytest.raises(ValueError) as ex:
        vectorsearch.add_texts(fake_texts)
    assert "`add_texts` is only supported for direct-access index." in str(ex.value)


def is_valid_uuid(val: str) -> bool:
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_add_texts() -> None:
    index = mock_index(DIRECT_ACCESS_INDEX)
    vectorsearch = DatabricksVectorSearch(
        index,
        embedding=DEFAULT_EMBEDDING_MODEL,
        text_column=DEFAULT_TEXT_COLUMN,
    )
    ids = [idx for idx, i in enumerate(fake_texts)]
    vectors = DEFAULT_EMBEDDING_MODEL.embed_documents(fake_texts)

    added_ids = vectorsearch.add_texts(fake_texts, ids=ids)
    index.upsert.assert_called_once_with(
        [
            {
                DEFAULT_PRIMARY_KEY: id_,
                DEFAULT_TEXT_COLUMN: text,
                DEFAULT_VECTOR_COLUMN: vector,
            }
            for text, vector, id_ in zip(fake_texts, vectors, ids)
        ]
    )
    assert len(added_ids) == len(fake_texts)
    assert added_ids == ids


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_add_texts_handle_single_text() -> None:
    index = mock_index(DIRECT_ACCESS_INDEX)
    vectorsearch = DatabricksVectorSearch(
        index,
        embedding=DEFAULT_EMBEDDING_MODEL,
        text_column=DEFAULT_TEXT_COLUMN,
    )
    vectors = DEFAULT_EMBEDDING_MODEL.embed_documents(fake_texts)

    added_ids = vectorsearch.add_texts(fake_texts[0])
    index.upsert.assert_called_once_with(
        [
            {
                DEFAULT_PRIMARY_KEY: id_,
                DEFAULT_TEXT_COLUMN: text,
                DEFAULT_VECTOR_COLUMN: vector,
            }
            for text, vector, id_ in zip(fake_texts, vectors, added_ids)
        ]
    )
    assert len(added_ids) == 1
    assert is_valid_uuid(added_ids[0])


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_add_texts_with_default_id() -> None:
    index = mock_index(DIRECT_ACCESS_INDEX)
    vectorsearch = default_databricks_vector_search(index)
    vectors = DEFAULT_EMBEDDING_MODEL.embed_documents(fake_texts)

    added_ids = vectorsearch.add_texts(fake_texts)
    index.upsert.assert_called_once_with(
        [
            {
                DEFAULT_PRIMARY_KEY: id_,
                DEFAULT_TEXT_COLUMN: text,
                DEFAULT_VECTOR_COLUMN: vector,
            }
            for text, vector, id_ in zip(fake_texts, vectors, added_ids)
        ]
    )
    assert len(added_ids) == len(fake_texts)
    assert all([is_valid_uuid(id_) for id_ in added_ids])


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_add_texts_with_metadata() -> None:
    index = mock_index(DIRECT_ACCESS_INDEX)
    vectorsearch = default_databricks_vector_search(index)
    vectors = DEFAULT_EMBEDDING_MODEL.embed_documents(fake_texts)
    metadatas = [{"feat1": str(i), "feat2": i + 1000} for i in range(len(fake_texts))]

    added_ids = vectorsearch.add_texts(fake_texts, metadatas=metadatas)
    index.upsert.assert_called_once_with(
        [
            {
                DEFAULT_PRIMARY_KEY: id_,
                DEFAULT_TEXT_COLUMN: text,
                DEFAULT_VECTOR_COLUMN: vector,
                **metadata,
            }
            for text, vector, id_, metadata in zip(
                fake_texts, vectors, added_ids, metadatas
            )
        ]
    )
    assert len(added_ids) == len(fake_texts)
    assert all([is_valid_uuid(id_) for id_ in added_ids])


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize(
    "index_details",
    [DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS, DIRECT_ACCESS_INDEX],
)
def test_embeddings_property(index_details: dict) -> None:
    index = mock_index(index_details)
    vectorsearch = default_databricks_vector_search(index)
    assert vectorsearch.embeddings == DEFAULT_EMBEDDING_MODEL


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize(
    "index_details",
    [DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS, DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS],
)
def test_delete_not_supported_for_delta_sync_index(index_details: dict) -> None:
    index = mock_index(index_details)
    vectorsearch = default_databricks_vector_search(index)
    with pytest.raises(ValueError) as ex:
        vectorsearch.delete(["some id"])
    assert "`delete` is only supported for direct-access index." in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_delete() -> None:
    index = mock_index(DIRECT_ACCESS_INDEX)
    vectorsearch = default_databricks_vector_search(index)

    vectorsearch.delete(["some id"])
    index.delete.assert_called_once_with(["some id"])


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_delete_fail_no_ids() -> None:
    index = mock_index(DIRECT_ACCESS_INDEX)
    vectorsearch = default_databricks_vector_search(index)

    with pytest.raises(ValueError) as ex:
        vectorsearch.delete()
    assert "ids must be provided." in str(ex.value)


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize("index_details", ALL_INDEXES)
def test_similarity_search(index_details: dict) -> None:
    index = mock_index(index_details)
    index.similarity_search.return_value = EXAMPLE_SEARCH_RESPONSE
    vectorsearch = default_databricks_vector_search(index)
    query = "foo"
    filters = {"some filter": True}
    limit = 7

    search_result = vectorsearch.similarity_search(query, k=limit, filters=filters)
    if index_details == DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS:
        index.similarity_search.assert_called_once_with(
            columns=[DEFAULT_PRIMARY_KEY, DEFAULT_TEXT_COLUMN],
            query_text=query,
            query_vector=None,
            filters=filters,
            num_results=limit,
        )
    else:
        index.similarity_search.assert_called_once_with(
            columns=[DEFAULT_PRIMARY_KEY, DEFAULT_TEXT_COLUMN],
            query_text=None,
            query_vector=DEFAULT_EMBEDDING_MODEL.embed_query(query),
            filters=filters,
            num_results=limit,
        )
    assert len(search_result) == len(fake_texts)
    assert sorted([d.page_content for d in search_result]) == sorted(fake_texts)
    assert all([DEFAULT_PRIMARY_KEY in d.metadata for d in search_result])


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize(
    "index_details", [DELTA_SYNC_INDEX_SELF_MANAGED_EMBEDDINGS, DIRECT_ACCESS_INDEX]
)
def test_similarity_search_by_vector(index_details: dict) -> None:
    index = mock_index(index_details)
    index.similarity_search.return_value = EXAMPLE_SEARCH_RESPONSE
    vectorsearch = default_databricks_vector_search(index)
    query_embedding = DEFAULT_EMBEDDING_MODEL.embed_query("foo")
    filters = {"some filter": True}
    limit = 7

    search_result = vectorsearch.similarity_search_by_vector(
        query_embedding, k=limit, filters=filters
    )
    index.similarity_search.assert_called_once_with(
        columns=[DEFAULT_PRIMARY_KEY, DEFAULT_TEXT_COLUMN],
        query_vector=query_embedding,
        filters=filters,
        num_results=limit,
    )
    assert len(search_result) == len(fake_texts)
    assert sorted([d.page_content for d in search_result]) == sorted(fake_texts)
    assert all([DEFAULT_PRIMARY_KEY in d.metadata for d in search_result])


@pytest.mark.requires("databricks", "databricks.vector_search")
@pytest.mark.parametrize("index_details", ALL_INDEXES)
def test_similarity_search_empty_result(index_details: dict) -> None:
    index = mock_index(index_details)
    index.similarity_search.return_value = {
        "manifest": {
            "column_count": 3,
            "columns": [
                {"name": DEFAULT_PRIMARY_KEY},
                {"name": DEFAULT_TEXT_COLUMN},
                {"name": "score"},
            ],
        },
        "result": {
            "row_count": 0,
            "data_array": [],
        },
        "next_page_token": "",
    }
    vectorsearch = default_databricks_vector_search(index)

    search_result = vectorsearch.similarity_search("foo")
    assert len(search_result) == 0


@pytest.mark.requires("databricks", "databricks.vector_search")
def test_similarity_search_by_vector_not_supported_for_managed_embedding() -> None:
    index = mock_index(DELTA_SYNC_INDEX_MANAGED_EMBEDDINGS)
    index.similarity_search.return_value = EXAMPLE_SEARCH_RESPONSE
    vectorsearch = default_databricks_vector_search(index)
    query_embedding = DEFAULT_EMBEDDING_MODEL.embed_query("foo")
    filters = {"some filter": True}
    limit = 7

    with pytest.raises(ValueError) as ex:
        vectorsearch.similarity_search_by_vector(
            query_embedding, k=limit, filters=filters
        )
    assert (
        "`similarity_search_by_vector` is not supported for index with "
        "Databricks-managed embeddings." in str(ex.value)
    )
