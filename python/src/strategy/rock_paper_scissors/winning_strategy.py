from random import Random
from typing import Any, Union

from pydantic import BaseModel, PrivateAttr

from ...common.custom_pydantic.config import BaseFrozenConfig
from .hand import Hand, Hand_, HandEnum
from .strategy import StrategyIF


class WinningStrategy(BaseModel, StrategyIF):
    _won: bool = PrivateAttr(default=False)
    _prev_hand: Hand_ = PrivateAttr()
    _random: Random = PrivateAttr()

    def __init__(
        self, seed: Union[int, float, str, bytes, bytearray, None] = None, **data: Any
    ) -> None:
        super().__init__(**data)
        self._random = Random(seed)

    def next_hand(self) -> Hand_:
        if not self._won:
            self._prev_hand = Hand.get_hand(self._random.choice(list(HandEnum)))
        return self._prev_hand

    def study(self, win: bool) -> None:
        self._won = win

    class Config(BaseFrozenConfig):
        pass
