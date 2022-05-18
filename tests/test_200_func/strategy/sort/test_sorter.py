from src.common.custom_pydantic.types import ComparableList
from src.strategy.sort.sorter import SorterABC


class DummySorter(SorterABC):
    def sort(self, data: ComparableList[int]) -> None:
        data.sort()


class TestSorterABC:
    def test_normal(self) -> None:
        data: ComparableList[int] = ComparableList[int]([3, 2, 1])
        sorter = DummySorter()

        sorter.sort(data)
        assert data == sorted(data)


class TestSelectionSorter:
    def test_normal(self) -> None:
        data: ComparableList[int] = ComparableList[int]([3, 2, 1])
        sorter = DummySorter()

        sorter.sort(data)
        assert data == sorted(data)
