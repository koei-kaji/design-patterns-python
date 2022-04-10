from typing import Any

from ...common.custom_pydantic.config import BaseFrozenConfig
from ...common.custom_pydantic.types import ComparableList
from .sorter import SorterABC


class SelectionSorter(SorterABC):
    def sort(self, data: ComparableList[Any]) -> None:
        for i in range(len(data)):
            _min = i
            for j in range(i + 1, len(data)):
                if data[j] < data[_min]:
                    _min = j
            data[_min], data[i] = data[i], data[_min]

    class Config(SorterABC.Config, BaseFrozenConfig):
        pass
