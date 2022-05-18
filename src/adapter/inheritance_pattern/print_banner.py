from typing import Any

from ..banner import Banner
from .print import PrintIF


class PrintBanner(Banner, PrintIF):
    def __init__(self, string: str, **data: Any) -> None:
        # pylint: disable=useless-super-delegation
        super().__init__(string=string, **data)

    def print_weak(self) -> None:
        self.show_with_paren()

    def print_strong(self) -> None:
        self.show_with_aster()

    class Config(Banner.Config):
        pass
