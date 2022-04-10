from typing import Generic, TypeVar

from pydantic.generics import GenericModel

from ...common.custom_pydantic.config import BaseFrozenConfig
from ...common.custom_pydantic.types import ComparableList
from .sorter import SorterABC

DataT = TypeVar("DataT")


class SortAndPrint(GenericModel, Generic[DataT]):
    data: ComparableList[DataT]
    sorter: SorterABC

    def execute(self) -> None:
        self.print()
        self.sorter.sort(self.data)
        self.print()

    def print(self) -> None:
        print("")
        for datum in self.data:
            print(f"{datum}, ", end="")
        print("")

    class Config(BaseFrozenConfig):
        pass
