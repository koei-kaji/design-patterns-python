from typing import Optional

from ..common.custom_pydantic.config import BaseFrozenConfig
from ..common.custom_pydantic.types import Char
from .border import BorderABC


class SideBorder(BorderABC):
    char_border: Char

    def get_columns(self) -> int:
        return 1 + self.display.get_columns() + 1

    def get_rows(self) -> int:
        return self.display.get_rows()

    def get_row_text(self, row: int) -> Optional[str]:
        return f"{self.char_border}{self.display.get_row_text(row)}{self.char_border}"

    class Config(BorderABC.Config, BaseFrozenConfig):
        pass
