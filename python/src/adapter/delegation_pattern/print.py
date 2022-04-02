import abc

from ...common.custom_pydantic.model import ABCModel


class PrintABC(ABCModel):
    @abc.abstractmethod
    def print_weak(self) -> None:
        pass

    @abc.abstractmethod
    def print_strong(self) -> None:
        pass
