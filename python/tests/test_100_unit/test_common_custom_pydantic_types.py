from typing import Any

import pytest
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError

from src.common.custom_pydantic.types import CharStr, ComparableList, ExtentionStr


class DummyChar(BaseModel):
    char: CharStr


class TestCharStr:
    def test_normal(self) -> None:
        model = DummyChar(char="a")
        assert model.char == "a"

    def test_exc_instantiation_with_int(self) -> None:
        with pytest.raises(ValidationError):
            DummyChar(char=9)

    def test_exc_with_empty(self) -> None:
        with pytest.raises(ValidationError):
            DummyChar(char="")

    def test_exc_with_2_chars(self) -> None:
        with pytest.raises(ValidationError):
            DummyChar(char="ab")


class DummyExt(BaseModel):
    ext: ExtentionStr


class TestExtentionStr:
    def test_normal(self) -> None:
        model = DummyExt(ext=".html")
        assert model.ext == ".html"

    def test_exc_instantiation_with_int(self) -> None:
        with pytest.raises(ValidationError):
            DummyExt(ext=999)

    def test_exc_not_match_regex(self) -> None:
        with pytest.raises(ValidationError):
            DummyExt(ext="hello")


class DummyComparable(BaseModel):
    data: ComparableList[Any]


class DummyIncomparable(BaseModel):
    pass


class TestComparableList:
    def test_normal(self) -> None:
        model = DummyComparable(data=[3, 2, 1])
        assert model.data == [3, 2, 1]

    def test_empty(self) -> None:
        model = DummyComparable(data=[])
        assert model.data == []

    def test_init_with_not_same_type(self) -> None:
        with pytest.raises(ValidationError):
            DummyComparable(data=[False, 1, "two"])

    def test_init_with_incomparable(self) -> None:
        with pytest.raises(ValidationError):
            DummyComparable(data=[DummyIncomparable])
