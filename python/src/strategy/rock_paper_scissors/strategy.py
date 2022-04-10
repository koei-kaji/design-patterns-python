import abc

from ...common.custom_pydantic.model import ABCModel
from .hand import Hand_


class StrategyABC(ABCModel):
    @abc.abstractmethod
    def next_hand(self) -> Hand_:
        pass

    @abc.abstractmethod
    def study(self, win: bool) -> None:
        pass
