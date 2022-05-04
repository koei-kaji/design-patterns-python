from __future__ import annotations

import abc
from typing import List, Optional

from pydantic import PrivateAttr

from ..common.custom_pydantic.model import ABCModel


class FileTreatmentException(Exception):
    pass


class EntryABC(ABCModel):
    _parent: Optional[EntryABC] = PrivateAttr(default=None)

    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_size(self) -> int:
        pass

    @abc.abstractmethod
    def _print_list(self, prefix: str) -> None:
        pass

    def add(self, entry: EntryABC) -> EntryABC:
        raise FileTreatmentException

    def print_list(self) -> None:
        self._print_list("")

    def get_full_name(self) -> str:
        entry_names: List[str] = []
        entry = self

        # pylint: disable=protected-access
        while entry._parent is not None:
            entry_names.insert(0, f"/{entry.get_name()}")
            entry = entry._parent
        entry_names.insert(0, f"/{entry.get_name()}")
        # pylint: enable=protected-access

        return "".join(entry_names)

    def __str__(self) -> str:
        return f"{self.get_name()} ({self.get_size()})"
