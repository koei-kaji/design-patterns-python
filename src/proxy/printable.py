import abc

from ..common.model import Interface


class PrintableIF(Interface):
    @abc.abstractmethod
    def set_printer_name(self, name: str) -> None:
        pass

    @abc.abstractmethod
    def get_printer_name(self) -> str:
        pass

    @abc.abstractmethod
    def print(self, string: str) -> None:
        pass
