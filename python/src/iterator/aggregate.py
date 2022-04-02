import abc

from ..common.custom_pydantic.model import ABCModel
from .iterator import IteratorABC


class AggregateABC(ABCModel):
    @abc.abstractmethod
    def iterator(self) -> IteratorABC:
        pass
