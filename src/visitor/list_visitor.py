from typing import Union

from multimethod import multimethod
from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .directory import Directory
from .file import File
from .visitor import VisitorABC


class ListVisitor(VisitorABC):
    _dir_current: str = PrivateAttr(default="")

    @multimethod
    def _visit(self, element: File) -> None:
        print(f"{self._dir_current}/{element}")

    @_visit.register
    def _(self, element: Directory) -> None:
        print(f"{self._dir_current}/{element}")
        dir_save = self._dir_current
        self._dir_current = f"{self._dir_current}/{element.get_name()}"
        for entry in element:
            entry.accept(self)
        self._dir_current = dir_save

    def visit(self, element: Union[File, Directory]) -> None:
        self._visit(element)

    class Config(VisitorABC.Config, BaseFrozenConfig):
        pass
