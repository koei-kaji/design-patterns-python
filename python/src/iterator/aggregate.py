import abc

from ..common.model import Interface
from .iterator import IteratorIF


class AggregateIF(Interface):
    @abc.abstractmethod
    def iterator(self) -> IteratorIF:
        pass
