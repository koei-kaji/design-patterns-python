from typing import Any

from pydantic import PrivateAttr

from ...common.custom_pydantic import BaseFrozenConfig
from ..banner import Banner
from .print import PrintABC


class PrintBanner(PrintABC):
    _banner: Banner = PrivateAttr()

    def __init__(self, string: str, **data: Any) -> None:
        super().__init__(**data)
        self._banner = Banner(string=string)

    def print_weak(self) -> None:
        self._banner.show_with_paren()

    def print_strong(self) -> None:
        self._banner.show_with_aster()

    class Config(BaseFrozenConfig):
        pass
