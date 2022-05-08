from ..common.custom_pydantic.types import CharStr
from .framework.product import ProductABC


class UnderlinePen(ProductABC):
    ulchar: CharStr

    def use(self, string: str) -> None:
        print("")
        print(f'"{string}"')
        print(f" {self.ulchar * len(string)} ")
