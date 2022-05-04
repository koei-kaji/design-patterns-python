from typing import List, Optional

from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .display import DisplayABC


class MultiStringDisplay(DisplayABC):
    _strings: List[str] = PrivateAttr(default=[])
    _max_length: int = PrivateAttr(default=0)

    def add(self, string: str) -> None:
        self._strings.append(string)

        length = len(string)
        if length > self._max_length:

            self._max_length = length

    def get_columns(self) -> int:
        return self._max_length

    def get_rows(self) -> int:
        return len(self._strings)

    def get_row_text(self, row: int) -> Optional[str]:
        return self._strings[row].ljust(self._max_length)

    class Config(DisplayABC.Config, BaseFrozenConfig):
        pass
