"""
Test of Astra DB document loader class `AstraDBLoader`

Required to run this test:
    - a recent `astrapy` Python package available
    - an Astra DB instance;
    - the two environment variables set:
        export ASTRA_DB_API_ENDPOINT="https://<DB-ID>-us-east1.apps.astra.datastax.com"
        export ASTRA_DB_APPLICATION_TOKEN="AstraCS:........."
    - optionally this as well (otherwise defaults are used):
        export ASTRA_DB_KEYSPACE="my_keyspace"
"""
import json
import os
import uuid

import pytest

from langchain_community.document_loaders.astradb import AstraDBLoader

ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")


def _has_env_vars() -> bool:
    return all([ASTRA_DB_APPLICATION_TOKEN, ASTRA_DB_API_ENDPOINT])


@pytest.fixture
def astra_db_collection():
    from astrapy.db import AstraDB

    astra_db = AstraDB(
        token=ASTRA_DB_APPLICATION_TOKEN,
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        namespace=ASTRA_DB_KEYSPACE,
    )
    collection_name = f"lc_test_loader_{str(uuid.uuid4()).split('-')[0]}"
    collection = astra_db.create_collection(collection_name)

    yield collection

    astra_db.delete_collection(collection_name)


@pytest.mark.requires("astrapy")
@pytest.mark.skipif(not _has_env_vars(), reason="Missing Astra DB env. vars")
class TestAstraDB:
    def test_astradb_loader(self, astra_db_collection) -> None:
        astra_db_collection.insert_many([{"foo": "bar", "baz": "qux"}] * 20)
        astra_db_collection.insert_many(
            [{"foo": "bar2", "baz": "qux"}] * 4 + [{"foo": "bar", "baz": "qux"}] * 4
        )

        loader = AstraDBLoader(
            astra_db_collection.collection_name,
            token=ASTRA_DB_APPLICATION_TOKEN,
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            namespace=ASTRA_DB_KEYSPACE,
            nb_prefetched=1,
            projection={"foo": 1},
            find_options={"limit": 22},
            filter_criteria={"foo": "bar"},
        )
        docs = loader.load()

        assert len(docs) == 22
        ids = set()
        for doc in docs:
            content = json.loads(doc.page_content)
            assert content["foo"] == "bar"
            assert "baz" not in content
            assert content["_id"] not in ids
            ids.add(content["_id"])
            assert doc.metadata == {
                "namespace": astra_db_collection.astra_db.namespace,
                "api_endpoint": astra_db_collection.astra_db.base_url,
                "collection": astra_db_collection.collection_name,
            }

    def test_extraction_function(self, astra_db_collection) -> None:
        astra_db_collection.insert_many([{"foo": "bar", "baz": "qux"}] * 20)

        loader = AstraDBLoader(
            astra_db_collection.collection_name,
            token=ASTRA_DB_APPLICATION_TOKEN,
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            namespace=ASTRA_DB_KEYSPACE,
            find_options={"limit": 30},
            extraction_function=lambda x: x["foo"],
        )
        docs = loader.lazy_load()
        doc = next(docs)

        assert doc.page_content == "bar"
