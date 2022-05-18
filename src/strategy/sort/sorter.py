import abc
from typing import Any

from ...common.custom_pydantic.model import ABCModel
from ...common.custom_pydantic.types import ComparableList


class SorterABC(ABCModel):
    @abc.abstractmethod
    def sort(self, data: ComparableList[Any]) -> None:
        pass
