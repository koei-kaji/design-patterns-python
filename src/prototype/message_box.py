from ..common.custom_pydantic.types import CharStr
from .framework.product import ProductABC


class MessageBox(ProductABC):
    decochar: CharStr

    def use(self, string: str) -> None:
        print("")
        print(f"{self.decochar * (len(string) + 4)}")
        print(f"{self.decochar} {string} {self.decochar}")
        print(f"{self.decochar * (len(string) + 4)}")
