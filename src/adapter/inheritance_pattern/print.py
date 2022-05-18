import abc

from ...common.model import Interface


class PrintIF(Interface):
    @abc.abstractmethod
    def print_weak(self) -> None:
        pass

    @abc.abstractmethod
    def print_strong(self) -> None:
        pass
