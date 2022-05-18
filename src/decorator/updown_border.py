from typing import Optional

from ..common.custom_pydantic.config import BaseFrozenConfig
from ..common.custom_pydantic.types import CharStr
from .border import BorderABC


class UpdownBorder(BorderABC):
    char_border: CharStr

    def get_columns(self) -> int:
        return self.display.get_columns()

    def get_rows(self) -> int:
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row: int) -> Optional[str]:
        if row == 0:
            return self.char_border * self.display.get_columns()
        elif row == self.display.get_rows() + 1:
            return self.char_border * self.display.get_columns()
        else:
            return self.display.get_row_text(row - 1)

    class Config(BorderABC.Config, BaseFrozenConfig):
        pass
