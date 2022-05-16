from __future__ import annotations

import abc
from typing import TYPE_CHECKING

from ..common.model import Interface

if TYPE_CHECKING:
    from .state import StateIF


class ContextIF(Interface):
    @abc.abstractmethod
    def set_clock(self, hour: int) -> None:
        pass

    @abc.abstractmethod
    def change_state(self, state: StateIF) -> None:
        pass

    @abc.abstractmethod
    def call_security_center(self, message: str) -> None:
        pass

    @abc.abstractmethod
    def record_log(self, message: str) -> None:
        pass
