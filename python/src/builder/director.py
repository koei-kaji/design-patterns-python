from pydantic import BaseModel

from ..common.custom_pydantic.config import BaseFrozenConfig
from .builder import BuilderABC


class Director(BaseModel):
    builder: BuilderABC

    def construct_(self) -> None:
        self.builder.make_title("Greeting")
        self.builder.make_string("朝から昼にかけて")
        self.builder.make_items(["おはようございます", "こんにちは"])
        self.builder.make_string("夜に")
        self.builder.make_items(["こんばんは", "おやすみなさい", "さようなら"])
        self.builder.close()

    class Config(BaseFrozenConfig):
        pass
