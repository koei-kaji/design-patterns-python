from __future__ import annotations

import abc
from typing import Iterator

from ..common.custom_pydantic.model import ABCModel
from .element import ElementIF
from .exc import FileTreatmentException


class EntryABC(ABCModel, ElementIF):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_size(self) -> int:
        pass

    def add(self, entry: EntryABC) -> EntryABC:
        raise FileTreatmentException

    def __iter__(self) -> Iterator[EntryABC]:  # type: ignore[override]
        raise FileTreatmentException

    def __next__(self) -> EntryABC:
        raise FileTreatmentException

    def __str__(self) -> str:
        return f"{self.get_name()} ({self.get_size()})"
