from typing import Any

from pydantic import StrictInt, StrictStr

from ...common.custom_pydantic.config import BaseFrozenConfig
from ..framework.product import ProductABC


class IDCard(ProductABC):
    owner: StrictStr

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        print(f"{self.owner}のカードを作ります")

    def use(self) -> None:
        print(f"{self.owner}のカードを使います")

    def get_owner(self) -> str:
        return self.owner

    class Config(ProductABC.Config, BaseFrozenConfig):
        pass


class IDCardWithSerial(ProductABC):
    owner: StrictStr
    serial: StrictInt

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        print(f"{self.owner}({self.serial})のカードを作ります")

    def use(self) -> None:
        print(f"{self.owner}({self.serial})のカードを使います")

    def get_owner(self) -> str:
        return self.owner

    def get_serial(self) -> int:
        return self.serial

    class Config(ProductABC.Config, BaseFrozenConfig):
        pass
