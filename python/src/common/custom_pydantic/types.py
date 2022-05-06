from __future__ import annotations

from typing import Callable, Iterator, List, TypeVar

from pydantic import ConstrainedStr
from pydantic.error_wrappers import ValidationError


class Char(ConstrainedStr):
    min_length = 1
    max_length = 1


ListType = TypeVar("ListType")


class ComparableList(list[ListType]):
    """
    ToDo:
        - FIXME: appendとかで更新される場合に型の違いを検出できない
        - FIXME: allow_mutation=Falseにしても参照型listのデータはチェックされない
    """

    @classmethod
    def __get_validators__(
        cls,
    ) -> Iterator[Callable[[list[ListType]], ComparableList[ListType]]]:
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def _validate_same_type(cls, v1: ListType, v2: ListType) -> None:
        if type(v1) is not type(v2):
            raise TypeError("must be same type")

    @classmethod
    def _validate_same_type_all(cls, v: List[ListType]) -> None:
        for datum in v[1:]:
            cls._validate_same_type(v[0], datum)

    @classmethod
    def _validate_comparable(cls, v1: ListType, v2: ListType) -> None:
        # NOTE: https://docs.python.org/3/library/functools.html#functools.total_ordering
        try:
            _ = v1 <= v2  # type: ignore[operator]
        except ValidationError as error:
            raise ValueError("must be comparable") from error

    @classmethod
    def validate(cls, v: List[ListType]) -> ComparableList[ListType]:
        if type(v) is not list:
            raise TypeError("list required")

        if v == []:
            return cls(v)

        cls._validate_same_type_all(v)
        cls._validate_comparable(v[0], v[0])

        return cls(v)

    def __repr__(self) -> str:
        return f"ComparableList({super().__repr__()})"
