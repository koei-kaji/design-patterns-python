from typing import Any

from pydantic import BaseModel, PrivateAttr


class Banner(BaseModel):
    _string: str = PrivateAttr()

    def __init__(self, string: str, **data: Any) -> None:
        super().__init__(**data)
        self._string = string

    def show_with_paren(self) -> None:
        print(f"({self._string})")

    def show_with_aster(self) -> None:
        print(f"*{self._string}*")
