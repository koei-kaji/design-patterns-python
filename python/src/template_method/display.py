import abc
from typing import final

from pydantic import StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from ..common.custom_pydantic.model import ABCModel
from ..common.custom_pydantic.types import CharStr


class DisplayABC(ABCModel):
    @abc.abstractmethod
    def open(self) -> None:
        pass

    @abc.abstractmethod
    def print(self) -> None:
        pass

    @abc.abstractmethod
    def close(self) -> None:
        pass

    @final
    def display(self) -> None:
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CharDisplay(DisplayABC):
    char: CharStr

    def open(self) -> None:
        print("<<", end="")

    def print(self) -> None:
        print(self.char, end="")

    def close(self) -> None:
        print(">>", end="\n")

    class Config(DisplayABC.Config, BaseFrozenConfig):
        pass


class StringDisplay(DisplayABC):
    string: StrictStr

    def open(self) -> None:
        print("")
        print(f"+{'-' * len(self.string)}+", end="\n")

    def print(self) -> None:
        print(f"|{self.string}|", end="\n")

    def close(self) -> None:
        print(f"+{'-' * len(self.string)}+")

    class Config(DisplayABC.Config, BaseFrozenConfig):
        pass
