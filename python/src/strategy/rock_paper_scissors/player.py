from pydantic import BaseModel, PrivateAttr, StrictStr

from ...common.custom_pydantic.config import BaseFrozenConfig
from .hand import Hand_
from .strategy import StrategyABC


class Player(BaseModel):
    name: StrictStr
    strategy: StrategyABC
    _count_win: int = PrivateAttr(default=0)
    _count_lose: int = PrivateAttr(default=0)
    _count_game: int = PrivateAttr(default=0)

    def next_hand(self) -> Hand_:
        return self.strategy.next_hand()

    def win(self) -> None:
        self.strategy.study(True)
        self._count_win += 1
        self._count_game += 1

    def lose(self) -> None:
        self.strategy.study(False)
        self._count_lose += 1
        self._count_game += 1

    def even(self) -> None:
        self._count_game += 1

    def __str__(self) -> str:
        return f"[{self.name}:{self._count_game} games, {self._count_win} win, {self._count_lose} lose]"

    class Config(BaseFrozenConfig):
        pass
