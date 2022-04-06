from typing import Final

from pydantic import StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .display_impl import DisplayImplABC

DEFAULT_ENCODING: Final[str] = "utf-8"


class FileDisplayImpl(DisplayImplABC):
    filename: StrictStr

    def raw_open(self) -> None:
        print(f"=-=-=-=-=-= {self.filename} =-=-=-=-=-=")

    def raw_print(self, encoding: str = DEFAULT_ENCODING) -> None:
        with open(self.filename, mode="r", encoding=encoding) as f:
            for line in f:
                print(f"> {line}", end="")
        print("")

    def raw_close(self) -> None:
        print("=-=-=-=-=-=")

    class Config(DisplayImplABC.Config, BaseFrozenConfig):
        pass
