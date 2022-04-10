from typing import Any

import pytest
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError

from src.common.custom_pydantic.types import ComparableList


class DummyModel(BaseModel):
    data: ComparableList[Any]


class DummyIncomparable(BaseModel):
    pass


class TestComparableList:
    def test_normal(self) -> None:
        model = DummyModel(data=[3, 2, 1])
        assert model.data == [3, 2, 1]

    def test_empty(self) -> None:
        model = DummyModel(data=[])
        assert model.data == []

    def test_init_with_not_same_type(self) -> None:
        with pytest.raises(ValidationError):
            DummyModel(data=[False, 1, "two"])

    def test_init_with_incomparable(self) -> None:
        with pytest.raises(ValidationError):
            DummyModel(data=[DummyIncomparable])
