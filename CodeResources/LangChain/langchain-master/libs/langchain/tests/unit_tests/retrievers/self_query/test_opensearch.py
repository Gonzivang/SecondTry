from langchain.chains.query_constructor.ir import (
    Comparator,
    Comparison,
    Operation,
    Operator,
    StructuredQuery,
)
from langchain.retrievers.self_query.opensearch import OpenSearchTranslator

DEFAULT_TRANSLATOR = OpenSearchTranslator()


def test_visit_comparison() -> None:
    comp = Comparison(comparator=Comparator.EQ, attribute="foo", value="10")
    expected = {"term": {"metadata.foo.keyword": "10"}}
    actual = DEFAULT_TRANSLATOR.visit_comparison(comp)
    assert expected == actual


def test_visit_operation() -> None:
    op = Operation(
        operator=Operator.AND,
        arguments=[
            Comparison(comparator=Comparator.GTE, attribute="bar", value=5),
            Comparison(comparator=Comparator.LT, attribute="bar", value=10),
            Comparison(comparator=Comparator.EQ, attribute="baz", value="abcd"),
        ],
    )
    expected = {
        "bool": {
            "must": [
                {"range": {"metadata.bar": {"gte": 5}}},
                {"range": {"metadata.bar": {"lt": 10}}},
                {"term": {"metadata.baz.keyword": "abcd"}},
            ]
        }
    }
    actual = DEFAULT_TRANSLATOR.visit_operation(op)
    assert expected == actual


def test_visit_structured_query() -> None:
    query = "What is the capital of France?"
    operation = Operation(
        operator=Operator.AND,
        arguments=[
            Comparison(comparator=Comparator.EQ, attribute="foo", value="20"),
            Operation(
                operator=Operator.OR,
                arguments=[
                    Comparison(comparator=Comparator.LTE, attribute="bar", value=7),
                    Comparison(
                        comparator=Comparator.LIKE, attribute="baz", value="abc"
                    ),
                ],
            ),
        ],
    )
    structured_query = StructuredQuery(query=query, filter=operation, limit=None)
    expected = (
        query,
        {
            "filter": {
                "bool": {
                    "must": [
                        {"term": {"metadata.foo.keyword": "20"}},
                        {
                            "bool": {
                                "should": [
                                    {"range": {"metadata.bar": {"lte": 7}}},
                                    {
                                        "fuzzy": {
                                            "metadata.baz": {
                                                "value": "abc",
                                            }
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        },
    )
    actual = DEFAULT_TRANSLATOR.visit_structured_query(structured_query)
    assert expected == actual


def test_visit_structured_query_with_date_range() -> None:
    query = "Who was the president of France in 1995?"
    operation = Operation(
        operator=Operator.AND,
        arguments=[
            Comparison(comparator=Comparator.EQ, attribute="foo", value="20"),
            Operation(
                operator=Operator.AND,
                arguments=[
                    Comparison(
                        comparator=Comparator.GTE,
                        attribute="timestamp",
                        value={"date": "1995-01-01", "type": "date"},
                    ),
                    Comparison(
                        comparator=Comparator.LT,
                        attribute="timestamp",
                        value={"date": "1996-01-01", "type": "date"},
                    ),
                ],
            ),
        ],
    )
    structured_query = StructuredQuery(query=query, filter=operation, limit=None)
    expected = (
        query,
        {
            "filter": {
                "bool": {
                    "must": [
                        {"term": {"metadata.foo.keyword": "20"}},
                        {
                            "bool": {
                                "must": [
                                    {
                                        "range": {
                                            "metadata.timestamp": {"gte": "1995-01-01"}
                                        }
                                    },
                                    {
                                        "range": {
                                            "metadata.timestamp": {"lt": "1996-01-01"}
                                        }
                                    },
                                ]
                            }
                        },
                    ]
                }
            }
        },
    )
    actual = DEFAULT_TRANSLATOR.visit_structured_query(structured_query)
    assert expected == actual


def test_visit_structured_query_with_date() -> None:
    query = "Who was the president of France on 1st of January 1995?"
    operation = Operation(
        operator=Operator.AND,
        arguments=[
            Comparison(comparator=Comparator.EQ, attribute="foo", value="20"),
            Comparison(
                comparator=Comparator.EQ,
                attribute="timestamp",
                value={"date": "1995-01-01", "type": "date"},
            ),
        ],
    )
    structured_query = StructuredQuery(query=query, filter=operation, limit=None)
    expected = (
        query,
        {
            "filter": {
                "bool": {
                    "must": [
                        {"term": {"metadata.foo.keyword": "20"}},
                        {"term": {"metadata.timestamp": "1995-01-01"}},
                    ]
                }
            }
        },
    )
    actual = DEFAULT_TRANSLATOR.visit_structured_query(structured_query)
    assert expected == actual
