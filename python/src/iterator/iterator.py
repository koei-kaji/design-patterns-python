import abc

from pydantic import BaseModel


class IteratorABC(BaseModel, abc.ABC):
    @abc.abstractmethod
    def has_next(self) -> bool:
        pass

    @abc.abstractmethod
    def next(self) -> object:
        pass
