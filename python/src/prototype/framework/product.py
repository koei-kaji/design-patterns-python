from __future__ import annotations

import abc
from typing import final

from pydantic import BaseModel


class ProductABC(BaseModel, abc.ABC):
    @abc.abstractmethod
    def use(self, string: str) -> None:
        pass

    @final
    def create_clone(self) -> ProductABC:
        return self.copy()
