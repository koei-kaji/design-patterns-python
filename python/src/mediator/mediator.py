import abc

from ..common.model import Interface


class MediatorIF(Interface):
    @abc.abstractmethod
    def create_colleagues(self) -> None:
        pass

    @abc.abstractmethod
    def colleague_changed(self) -> None:
        pass
