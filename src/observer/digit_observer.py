from time import sleep

from pydantic import BaseModel

from ..common.custom_pydantic.config import BaseFrozenConfig
from .number_generator import NumberGeneratorABC
from .observer import ObserverIF


class DigitObserver(BaseModel, ObserverIF):
    def subscribe(self, generator: NumberGeneratorABC) -> None:
        print(f"DigitObserver:{generator.get_number()}")
        sleep(0.1)

    class Config(BaseFrozenConfig):
        pass
