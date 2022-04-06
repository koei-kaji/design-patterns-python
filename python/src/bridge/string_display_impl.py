from pydantic import StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .display_impl import DisplayImplABC


class StringDisplayImpl(DisplayImplABC):
    string: StrictStr

    def raw_open(self) -> None:
        self._print_line()

    def raw_print(self) -> None:
        print(f"|{self.string}|")

    def raw_close(self) -> None:
        self._print_line()

    def _print_line(self) -> None:
        print(f"+{'-' * len(self.string)}+")

    class Config(DisplayImplABC.Config, BaseFrozenConfig):
        pass
