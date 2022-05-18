from pathlib import Path
from typing import Any, Final

from pydantic import BaseModel, PrivateAttr, StrictStr

from ..common.custom_pydantic.types import CharStr

DIR_BASE: Final[Path] = Path(__file__).parent
DIR_FONT: Final[Path] = DIR_BASE / "font_data"


class BigChar(BaseModel):
    char: CharStr
    _font_data: StrictStr = PrivateAttr()

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        file_path = str(DIR_FONT / f"big{self.char}.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                self._font_data = "\n".join(lines)
        except FileNotFoundError:
            self._font_data = f"{self.char}?"

    def print(self) -> None:
        print(self._font_data)
