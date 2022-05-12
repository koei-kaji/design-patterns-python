from __future__ import annotations

import abc
from typing import TYPE_CHECKING, List

from pydantic import PrivateAttr

from ..common.custom_pydantic.model import ABCModel

if TYPE_CHECKING:
    from .observer import ObserverIF


class NumberGeneratorABC(ABCModel):
    _observers: List[ObserverIF] = PrivateAttr(default=[])

    def add_observer(self, observer: ObserverIF) -> None:
        self._observers.append(observer)

    def delete_observer(self, observer: ObserverIF) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.subscribe(self)

    @abc.abstractmethod
    def get_number(self) -> int:
        pass

    @abc.abstractmethod
    def publish(self) -> None:
        pass
