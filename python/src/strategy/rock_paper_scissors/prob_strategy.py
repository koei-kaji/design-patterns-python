from random import Random
from typing import Any, List, Union

from pydantic import PrivateAttr

from ...common.custom_pydantic.config import BaseFrozenConfig
from .hand import Hand, Hand_, HandEnum
from .strategy import StrategyABC


class ProbStrategy(StrategyABC):
    _random: Random = PrivateAttr()
    _prev_hand: HandEnum = PrivateAttr()
    _current_hand: HandEnum = PrivateAttr()
    _history: List[List[int]] = PrivateAttr(default=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    def __init__(
        self, seed: Union[int, float, str, bytes, bytearray, None] = None, **data: Any
    ) -> None:
        super().__init__(**data)
        self._random = Random(seed)
        self._prev_hand = self._random.choice(list(HandEnum))
        self._current_hand = self._random.choice(list(HandEnum))

    def _get_sum(self, hand: HandEnum) -> int:
        sum_ = sum(self._history[hand.value])
        return sum_

    def next_hand(self) -> Hand_:
        bet = self._random.randint(0, self._get_sum(self._current_hand))

        hand: HandEnum
        if bet < self._history[self._current_hand.value][0]:
            hand = HandEnum.ROCK
        elif bet < sum(self._history[self._current_hand.value][:2]):
            hand = HandEnum.SCISSORS
        else:
            hand = HandEnum.PAPER

        self._prev_hand = self._current_hand
        self._current_hand = hand

        return Hand.get_hand(self._current_hand)

    def study(self, win: bool) -> None:
        if win:
            self._history[self._prev_hand.value][self._current_hand.value] += 1
        else:
            self._history[self._prev_hand.value][
                (self._current_hand.value + 1) % 3
            ] += 1
            self._history[self._prev_hand.value][
                (self._current_hand.value + 2) % 3
            ] += 1

    class Config(StrategyABC.Config, BaseFrozenConfig):
        pass
