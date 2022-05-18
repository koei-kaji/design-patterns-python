import abc

from ..common.model import Interface


class IteratorIF(Interface):
    @abc.abstractmethod
    def has_next(self) -> bool:
        pass

    @abc.abstractmethod
    def next(self) -> object:
        pass
