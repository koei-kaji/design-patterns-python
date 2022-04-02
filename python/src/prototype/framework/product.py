from __future__ import annotations

import abc
from typing import final

from ...common.custom_pydantic.model import ABCModel


class ProductABC(ABCModel):
    @abc.abstractmethod
    def use(self, string: str) -> None:
        pass

    @final
    def create_clone(self) -> ProductABC:
        return self.copy()
