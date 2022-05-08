from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .entry import EntryABC

if TYPE_CHECKING:
    from .visitor import VisitorABC


class File(EntryABC):
    name: StrictStr
    size: StrictInt

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def accept(self, visitor: VisitorABC) -> None:
        visitor.visit(self)

    class Config(EntryABC.Config, BaseFrozenConfig):
        pass
