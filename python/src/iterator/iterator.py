import abc

from ..common.custom_pydantic.model import ABCModel


class IteratorABC(ABCModel):
    @abc.abstractmethod
    def has_next(self) -> bool:
        pass

    @abc.abstractmethod
    def next(self) -> object:
        pass
