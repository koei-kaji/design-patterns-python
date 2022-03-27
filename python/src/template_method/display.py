import abc
from typing import Any, final

from pydantic import BaseModel, PrivateAttr

from .custom_type import Char


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
    _char: Char = PrivateAttr()

    def __init__(self, char: Char, **data: Any) -> None:
        super().__init__(**data)
        self._char = char

    def open(self) -> None:
        print("<<", end="")

    def print(self) -> None:
        print(self._char, end="")

    def close(self) -> None:
        print(">>", end="\n")


class StringDisplay(DisplayABC):
    _string: str = PrivateAttr()

    def __init__(self, string: str, **data: Any) -> None:
        super().__init__(**data)
        self._string = string

    def open(self) -> None:
        print("")
        print(f"+{'-' * len(self._string)}+", end="\n")

    def print(self) -> None:
        print(f"|{self._string}|", end="\n")

    def close(self) -> None:
        print(f"+{'-' * len(self._string)}+")
