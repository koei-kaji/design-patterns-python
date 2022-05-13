from random import Random

from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .number_generator import NumberGeneratorABC


class RandomNumberGenerator(NumberGeneratorABC):
    _random: Random = PrivateAttr(default_factory=Random)
    _number: int = PrivateAttr()

    def get_number(self) -> int:
        return self._number

    def publish(self) -> None:
        for _ in range(20):
            self._number = self._random.randint(0, 50)
            self.notify_observers()

    class Config(NumberGeneratorABC.Config, BaseFrozenConfig):
        pass
