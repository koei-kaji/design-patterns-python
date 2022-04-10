from random import Random
from typing import Any, Union

from pydantic import PrivateAttr

from ...common.custom_pydantic.config import BaseFrozenConfig
from .hand import Hand, Hand_, HandEnum
from .strategy import StrategyABC


class RandomStrategy(StrategyABC):
    _random: Random = PrivateAttr()

    def __init__(
        self, seed: Union[int, float, str, bytes, bytearray, None] = None, **data: Any
    ) -> None:
        super().__init__(**data)
        self._random = Random(seed)

    def next_hand(self) -> Hand_:
        return Hand.get_hand(self._random.choice(list(HandEnum)))

    def study(self, win: bool) -> None:
        pass

    class Config(StrategyABC.Config, BaseFrozenConfig):
        pass
