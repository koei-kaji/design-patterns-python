from typing import Optional

from pydantic import StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .display import DisplayABC


class StringDisplay(DisplayABC):
    string: StrictStr

    def get_columns(self) -> int:
        return len(self.string)

    def get_rows(self) -> int:
        return 1

    def get_row_text(self, row: int) -> Optional[str]:
        if row == 0:
            return self.string
        else:
            return None

    class Config(DisplayABC.Config, BaseFrozenConfig):
        pass
