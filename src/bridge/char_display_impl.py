from ..common.custom_pydantic.config import BaseFrozenConfig
from ..common.custom_pydantic.types import CharStr
from .display_impl import DisplayImplABC


class CharDisplayImpl(DisplayImplABC):
    head: CharStr
    body: CharStr
    foot: CharStr

    def raw_open(self) -> None:
        print(self.head, end="")

    def raw_print(self) -> None:
        print(self.body, end="")

    def raw_close(self) -> None:
        print(self.foot)

    class Config(DisplayImplABC.Config, BaseFrozenConfig):
        pass
