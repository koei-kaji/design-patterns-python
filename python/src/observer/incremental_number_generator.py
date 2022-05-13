from typing import Any

from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .number_generator import NumberGeneratorABC


class IncrementalNumberGenerator(NumberGeneratorABC):
    start: int
    end: int
    increment: int
    _number: int = PrivateAttr()

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self._number = self.start

    def get_number(self) -> int:
        return self._number

    def publish(self) -> None:
        while self._number < self.end:
            self.notify_observers()
            self._number += self.increment

    class Config(NumberGeneratorABC.Config, BaseFrozenConfig):
        pass
