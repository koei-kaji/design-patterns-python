from pydantic import BaseModel

from ..common.custom_pydantic.config import BaseFrozenConfig


class Banner(BaseModel):
    string: str

    def show_with_paren(self) -> None:
        print(f"({self.string})")

    def show_with_aster(self) -> None:
        print(f"*{self.string}*")

    class Config(BaseFrozenConfig):
        pass
