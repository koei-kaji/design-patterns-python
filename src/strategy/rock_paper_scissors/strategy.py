import abc

from ...common.model import Interface
from .hand import Hand_


class StrategyIF(Interface):
    @abc.abstractmethod
    def next_hand(self) -> Hand_:
        pass

    @abc.abstractmethod
    def study(self, win: bool) -> None:
        pass
