import abc

from src.mediator.mediator import MediatorIF

from ..common.model import Interface


class ColleagueIF(Interface):
    @abc.abstractmethod
    def set_mediator(self, mediator: MediatorIF) -> None:
        pass

    @abc.abstractmethod
    def set_colleague_enabled(self, enabled: bool) -> None:
        pass
