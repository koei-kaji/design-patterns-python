from typing import Any, final

from pydantic import BaseModel, PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .display_impl import DisplayImplABC


class Display(BaseModel):
    _impl: DisplayImplABC = PrivateAttr()

    def __init__(self, impl: DisplayImplABC, **data: Any) -> None:
        super().__init__(**data)
        self._impl = impl

    def open(self) -> None:
        self._impl.raw_open()

    def print(self) -> None:
        self._impl.raw_print()

    def close(self) -> None:
        self._impl.raw_close()

    @final
    def display(self) -> None:
        self.open()
        self.print()
        self.close()

    class Config(BaseFrozenConfig):
        pass
