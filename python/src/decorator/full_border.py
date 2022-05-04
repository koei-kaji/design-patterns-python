from typing import Optional

from ..common.custom_pydantic.config import BaseFrozenConfig
from .border import BorderABC


class FullBorder(BorderABC):
    def get_columns(self) -> int:
        return 1 + self.display.get_columns() + 1

    def get_rows(self) -> int:
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row: int) -> Optional[str]:
        if row == 0:
            return f"+{'-' * self.display.get_columns()}+"
        elif row == self.display.get_rows() + 1:
            return f"+{'-' * self.display.get_columns()}+"
        else:
            return f"|{self.display.get_row_text(row - 1)}|"

    class Config(BorderABC.Config, BaseFrozenConfig):
        pass
