from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Union

from ..common.custom_pydantic.model import ABCModel

if TYPE_CHECKING:
    from .directory import Directory
    from .file import File


class VisitorABC(ABCModel):
    @abc.abstractmethod
    def visit(self, element: Union[File, Directory]) -> None:
        pass
