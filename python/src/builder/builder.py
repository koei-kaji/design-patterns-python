import abc
from typing import List

from ..common.custom_pydantic.model import ABCModel


class BuilderABC(ABCModel):
    @abc.abstractmethod
    def make_title(self, title: str) -> None:
        pass

    @abc.abstractmethod
    def make_string(self, string: str) -> None:
        pass

    @abc.abstractmethod
    def make_items(self, items: List[str]) -> None:
        pass

    @abc.abstractmethod
    def close(self) -> None:
        pass
