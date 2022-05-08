from __future__ import annotations

from typing import Iterable, Iterator, List, Union

from multimethod import multimethod
from pydantic import PrivateAttr, StrictBool, StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .entry import EntryABC
from .file import File
from .visitor import VisitorABC


class Directory(EntryABC, Iterable[EntryABC]):
    name: StrictStr
    use_visitor: StrictBool = False
    _entries: List[EntryABC] = PrivateAttr(default=[])
    _index: int = PrivateAttr()

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        if self.use_visitor:
            visitor = SizeVisitor()
            self.accept(visitor)
            return visitor.get_size()

        size: int = 0
        for entry in self._entries:
            size += entry.get_size()
        return size

    def add(self, entry: EntryABC) -> EntryABC:
        self._entries.append(entry)
        return self

    def __iter__(self) -> Iterator[EntryABC]:  # type: ignore[override]
        self._index = 0
        return self

    def __next__(self) -> EntryABC:
        if self._index == len(self._entries):
            raise StopIteration()
        entry = self._entries[self._index]
        self._index += 1

        return entry

    def accept(self, visitor: VisitorABC) -> None:
        visitor.visit(self)

    class Config(EntryABC.Config, BaseFrozenConfig):
        pass


# TODO: 循環参照になるのでこのファイルに記載。うまいこと分離できる？
class SizeVisitor(VisitorABC):
    _size: int = PrivateAttr(default=0)

    @multimethod
    def _visit(self, element: File) -> None:
        size = element.get_size()
        self._size += size

    @_visit.register
    def _(self, element: Directory) -> None:
        for entry in element:
            self._visit(entry)

    def visit(self, element: Union[File, Directory]) -> None:
        self._visit(element)

    def get_size(self) -> int:
        return self._size

    class Config(VisitorABC.Config, BaseFrozenConfig):
        pass
