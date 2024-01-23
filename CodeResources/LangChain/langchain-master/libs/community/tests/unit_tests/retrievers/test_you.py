import json
import os
from unittest import mock

from langchain_core.documents import Document
from requests import Response

from langchain_community.retrievers.you import YouRetriever


class TestYouRetriever:
    def test_get_relevant_documents(self) -> None:
        os.environ["YDC_API_KEY"] = "MOCK KEY!"
        retriever = YouRetriever()

        with mock.patch("requests.get") as mock_get:
            fixture = {"hits": [{"snippets": ["yo"]}, {"snippets": ["bird up"]}]}
            response = Response()
            response._content = bytes(json.dumps(fixture).encode("utf-8"))
            mock_get.return_value = response

            actual = retriever.get_relevant_documents("test")
            assert actual == [
                Document(page_content="yo"),
                Document(page_content="bird up"),
            ]
