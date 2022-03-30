import abc
from typing import final

from pydantic import BaseModel, StrictStr

from ..common.custom_pydantic import BaseFrozenConfig
from .types import Char


class DisplayABC(BaseModel, abc.ABC):
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
    char: Char

    def open(self) -> None:
        print("<<", end="")

    def print(self) -> None:
        print(self.char, end="")

    def close(self) -> None:
        print(">>", end="\n")

    class Config(BaseFrozenConfig):
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

    class Config(BaseFrozenConfig):
        pass
