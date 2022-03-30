import abc

from pydantic import BaseModel

from .iterator import IteratorABC


class AggregateABC(BaseModel, abc.ABC):
    @abc.abstractmethod
    def iterator(self) -> IteratorABC:
        pass
