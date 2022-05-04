import abc
from typing import Optional, final

from ..common.custom_pydantic.model import ABCModel


class DisplayABC(ABCModel):
    @abc.abstractmethod
    def get_columns(self) -> int:
        pass

    @abc.abstractmethod
    def get_rows(self) -> int:
        pass

    @abc.abstractmethod
    def get_row_text(self, row: int) -> Optional[str]:
        pass

    @final
    def show(self) -> None:
        for i in range(self.get_rows()):
            print(self.get_row_text(i))
