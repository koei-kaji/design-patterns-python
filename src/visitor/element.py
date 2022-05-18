from __future__ import annotations

import abc
from typing import TYPE_CHECKING

from ..common.model import Interface

if TYPE_CHECKING:
    from .visitor import VisitorABC


class ElementIF(Interface):
    @abc.abstractmethod
    def accept(self, visitor: VisitorABC) -> None:
        pass


class ElementList(list[ElementIF], ElementIF):
    def accept(self, visitor: VisitorABC) -> None:
        for element in self:
            element.accept(visitor)
