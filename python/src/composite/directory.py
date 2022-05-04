from typing import List

from pydantic import PrivateAttr, StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .entry import EntryABC


class Directory(EntryABC):
    name: StrictStr
    _directory: List[EntryABC] = PrivateAttr(default=[])

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        size: int = 0
        for entry in self._directory:
            size += entry.get_size()

        return size

    def add(self, entry: EntryABC) -> EntryABC:
        self._directory.append(entry)
        entry._parent = self  # pylint: disable=protected-access
        return self

    def _print_list(self, prefix: str) -> None:
        print(f"{prefix}/{self}")
        for entry in self._directory:
            entry._print_list(  # pylint: disable=protected-access
                f"{prefix}/{self.name}"
            )

    class Config(EntryABC.Config, BaseFrozenConfig):
        pass
