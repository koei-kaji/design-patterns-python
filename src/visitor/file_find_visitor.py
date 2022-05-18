from __future__ import annotations

from typing import List, Union

from multimethod import multimethod
from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from ..common.custom_pydantic.types import ExtentionStr
from .directory import Directory
from .file import File
from .visitor import VisitorABC


class FileFindVisitor(VisitorABC):
    ext: ExtentionStr
    _found_files: List[File] = PrivateAttr(default=[])

    @multimethod
    def _visit(self, element: File) -> None:
        file_name = element.get_name()
        if file_name.endswith(self.ext):
            self._found_files.append(element)

    @_visit.register
    def _(self, element: Directory) -> None:
        for entry in element:
            self._visit(entry)

    def visit(self, element: Union[File, Directory]) -> None:
        self._visit(element)

    def get_found_files(self) -> List[File]:
        return self._found_files

    class Config(VisitorABC.Config, BaseFrozenConfig):
        pass
