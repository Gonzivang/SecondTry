import warnings
from typing import Any, Dict

import pytest

from langchain_core._api.beta_decorator import beta, warn_beta
from langchain_core.pydantic_v1 import BaseModel


@pytest.mark.parametrize(
    "kwargs, expected_message",
    [
        (
            {
                "name": "OldClass",
                "obj_type": "class",
            },
            "The class `OldClass` is in beta. It is actively being worked on, so the "
            "API may change.",
        ),
        (
            {
                "message": "This is a custom message",
                "name": "FunctionA",
                "obj_type": "",
                "addendum": "",
            },
            "This is a custom message",
        ),
        (
            {
                "message": "",
                "name": "SomeFunction",
                "obj_type": "",
                "addendum": "Please migrate your code.",
            },
            "`SomeFunction` is in beta. It is actively being worked on, so the API may "
            "change. Please migrate your code.",
        ),
    ],
)
def test_warn_beta(kwargs: Dict[str, Any], expected_message: str) -> None:
    """Test warn beta."""
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")

        warn_beta(**kwargs)

        assert len(warning_list) == 1
        warning = warning_list[0].message
        assert str(warning) == expected_message


@beta()
def beta_function() -> str:
    """original doc"""
    return "This is a beta function."


class ClassWithBetaMethods:
    def __init__(self) -> None:
        """original doc"""
        pass

    @beta()
    def beta_method(self) -> str:
        """original doc"""
        return "This is a beta method."

    @classmethod
    @beta()
    def beta_classmethod(cls) -> str:
        """original doc"""
        return "This is a beta classmethod."

    @staticmethod
    @beta()
    def beta_staticmethod() -> str:
        """original doc"""
        return "This is a beta staticmethod."

    @property
    @beta()
    def beta_property(self) -> str:
        """original doc"""
        return "This is a beta property."


def test_beta_function() -> None:
    """Test beta function."""
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")
        assert beta_function() == "This is a beta function."
        assert len(warning_list) == 1
        warning = warning_list[0].message
        assert str(warning) == (
            "The function `beta_function` is in beta. It is actively being worked on, "
            "so the API may change."
        )

        doc = beta_function.__doc__
        assert isinstance(doc, str)
        assert doc.startswith("[*Beta*]  original doc")


def test_beta_method() -> None:
    """Test beta method."""
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")
        obj = ClassWithBetaMethods()
        assert obj.beta_method() == "This is a beta method."
        assert len(warning_list) == 1
        warning = warning_list[0].message
        assert str(warning) == (
            "The function `beta_method` is in beta. It is actively being worked on, so "
            "the API may change."
        )

        doc = obj.beta_method.__doc__
        assert isinstance(doc, str)
        assert doc.startswith("[*Beta*]  original doc")


def test_beta_classmethod() -> None:
    """Test beta classmethod."""
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")
        ClassWithBetaMethods.beta_classmethod()
        assert len(warning_list) == 1
        warning = warning_list[0].message
        assert str(warning) == (
            "The function `beta_classmethod` is in beta. It is actively being worked "
            "on, so the API may change."
        )

        doc = ClassWithBetaMethods.beta_classmethod.__doc__
        assert isinstance(doc, str)
        assert doc.startswith("[*Beta*]  original doc")


def test_beta_staticmethod() -> None:
    """Test beta staticmethod."""
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")
        assert (
            ClassWithBetaMethods.beta_staticmethod() == "This is a beta staticmethod."
        )
        assert len(warning_list) == 1
        warning = warning_list[0].message

        assert str(warning) == (
            "The function `beta_staticmethod` is in beta. It is actively being worked "
            "on, so the API may change."
        )
        doc = ClassWithBetaMethods.beta_staticmethod.__doc__
        assert isinstance(doc, str)
        assert doc.startswith("[*Beta*]  original doc")


def test_beta_property() -> None:
    """Test beta staticmethod."""
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")

        obj = ClassWithBetaMethods()
        assert obj.beta_property == "This is a beta property."

        assert len(warning_list) == 1
        warning = warning_list[0].message

        assert str(warning) == (
            "The function `beta_property` is in beta. It is actively being worked on, "
            "so the API may change."
        )
        doc = ClassWithBetaMethods.beta_property.__doc__
        assert isinstance(doc, str)
        assert doc.startswith("[*Beta*]  original doc")


def test_whole_class_deprecation() -> None:
    """Test whole class deprecation."""

    # Test whole class deprecation
    @beta()
    class BetaClass:
        def __init__(self) -> None:
            """original doc"""
            pass

        @beta()
        def beta_method(self) -> str:
            """original doc"""
            return "This is a beta method."

    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")

        obj = BetaClass()
        assert obj.beta_method() == "This is a beta method."

        assert len(warning_list) == 2
        warning = warning_list[0].message
        assert str(warning) == (
            "The class `BetaClass` is in beta. It is actively being worked on, so the "
            "API may change."
        )

        warning = warning_list[1].message
        assert str(warning) == (
            "The function `beta_method` is in beta. It is actively being worked on, so "
            "the API may change."
        )


# Tests with pydantic models
class MyModel(BaseModel):
    @beta()
    def beta_method(self) -> str:
        """original doc"""
        return "This is a beta method."


def test_beta_method_pydantic() -> None:
    """Test beta method."""
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")
        obj = MyModel()
        assert obj.beta_method() == "This is a beta method."
        assert len(warning_list) == 1
        warning = warning_list[0].message
        assert str(warning) == (
            "The function `beta_method` is in beta. It is actively being worked on, so "
            "the API may change."
        )

        doc = obj.beta_method.__doc__
        assert isinstance(doc, str)
        assert doc.startswith("[*Beta*]  original doc")
