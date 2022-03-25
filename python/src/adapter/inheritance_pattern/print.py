import abc

from pydantic import BaseModel


class PrintABC(BaseModel, abc.ABC):
    @abc.abstractmethod
    def print_weak(self) -> None:
        pass

    @abc.abstractmethod
    def print_strong(self) -> None:
        pass
