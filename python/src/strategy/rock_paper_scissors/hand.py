from __future__ import annotations

from enum import IntEnum
from typing import Any, List

from pydantic import BaseModel, PrivateAttr


class InstantiationException(Exception):
    pass


class HandEnum(IntEnum):
    ROCK = 0
    SCISSORS = 1
    PAPER = 2


class ResultEnum(IntEnum):
    DEFEAT = -1
    DRAW = 0
    VICTORY = 1


class Hand_(BaseModel):

    _hand: HandEnum = PrivateAttr()
    _hand_signs: List[Hand_] = []

    # pylint: disable=unused-argument
    def __new__(cls, hand_enum: HandEnum, **_: Any) -> Hand_:
        if len(cls._hand_signs) >= 3:
            raise InstantiationException(
                "Instance of this class has been already created three times"
            )
        cls._hand_signs.append(super().__new__(cls))
        return cls._hand_signs[-1]

    # pylint: enable=unused-argument

    def __init__(self, hand_enum: HandEnum, **data: Any) -> None:
        super().__init__(**data)
        self._hand = hand_enum

    def __str__(self) -> str:
        return self._hand.name.capitalize()

    def get_hand(self, hand: HandEnum) -> Hand_:
        return self._hand_signs[hand.value]

    def _fight(self, hand: Hand_) -> ResultEnum:
        # pylint: disable=protected-access
        if id(self) == id(hand):
            return ResultEnum.DRAW
        elif (self._hand.value + 1) % 3 == hand._hand.value:
            return ResultEnum.VICTORY
        else:
            return ResultEnum.DEFEAT
        # pylint: enable=protected-access

    def is_stronger_than(self, hand: Hand_) -> bool:
        return self._fight(hand) == ResultEnum.VICTORY

    def is_weaker_than(self, hand: Hand_) -> bool:
        return self._fight(hand) == ResultEnum.DEFEAT


Hand = [Hand_(hand_enum=hand) for hand in HandEnum][0]
