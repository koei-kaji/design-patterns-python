from ..common.custom_pydantic.types import Char
from .framework.product import ProductABC


class UnderlinePen(ProductABC):
    ulchar: Char

    def use(self, string: str) -> None:
        print("")
        print(f'"{string}"')
        print(f" {self.ulchar * len(string)} ")
