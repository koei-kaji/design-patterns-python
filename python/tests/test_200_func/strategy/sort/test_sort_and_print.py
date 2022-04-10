from typing import Final, List

from src.common.custom_pydantic.types import ComparableList
from src.strategy.sort.selection_sorter import SelectionSorter
from src.strategy.sort.sort_and_print import SortAndPrint


class TestSelectionSort:
    def test_normal(self) -> None:
        DATA: Final[List[str]] = ["Dumpty", "Bowman", "Carrol", "Elfland", "Alice"]

        s_and_p = SortAndPrint[str](data=DATA, sorter=SelectionSorter())
        s_and_p.execute()

        assert s_and_p.data == sorted(DATA)
