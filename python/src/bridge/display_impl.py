import abc

from ..common.custom_pydantic.model import ABCModel


class DisplayImplABC(ABCModel):
    @abc.abstractmethod
    def raw_open(self) -> None:
        pass

    @abc.abstractmethod
    def raw_print(self) -> None:
        pass

    @abc.abstractmethod
    def raw_close(self) -> None:
        pass
