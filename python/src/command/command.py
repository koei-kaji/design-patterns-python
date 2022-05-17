import abc

from ..common.model import Interface


class CommandIF(Interface):
    @abc.abstractmethod
    def execute(self) -> None:
        pass
