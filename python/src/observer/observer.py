from __future__ import annotations

import abc
from typing import TYPE_CHECKING

from ..common.model import Interface

if TYPE_CHECKING:
    from .number_generator import NumberGeneratorABC


class ObserverIF(Interface):
    @abc.abstractmethod
    def subscribe(self, generator: NumberGeneratorABC) -> None:
        pass
