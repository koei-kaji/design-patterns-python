from __future__ import annotations

import abc
from typing import TYPE_CHECKING, cast

from ..common.model import Interface

if TYPE_CHECKING:
    from .context import ContextIF

from ..common.custom_pydantic.config import BaseFrozenConfig
from ..singleton._singleton import BaseSingleton
from .context import ContextIF


class StateIF(Interface):
    @abc.abstractmethod
    def do_clock(self, context: ContextIF, hour: int) -> None:
        pass

    @abc.abstractmethod
    def do_use(self, context: ContextIF) -> None:
        pass

    @abc.abstractmethod
    def do_alarm(self, context: ContextIF) -> None:
        pass

    @abc.abstractmethod
    def do_phone(self, context: ContextIF) -> None:
        pass

    @abc.abstractmethod
    def do_lift(self, context: ContextIF, hour: int) -> None:
        pass


def _switch_context_by_hour(context: ContextIF, hour: int) -> None:
    if 12 <= hour < 13:
        context.change_state(cast(StateIF, NoonState.get_instance()))
    elif 9 <= hour < 17:
        context.change_state(cast(StateIF, DayState.get_instance()))
    elif hour < 9 or 17 <= hour:
        context.change_state(cast(StateIF, NightState.get_instance()))


class DayState(BaseSingleton, StateIF):
    def do_clock(self, context: ContextIF, hour: int) -> None:
        _switch_context_by_hour(context, hour)

    def do_use(self, context: ContextIF) -> None:
        context.record_log("金庫使用（昼間）")

    def do_alarm(self, context: ContextIF) -> None:
        context.call_security_center("非常ベル（昼間）")
        context.change_state(cast(StateIF, UrgentState.get_instance()))

    def do_phone(self, context: ContextIF) -> None:
        context.call_security_center("通常の通話（昼間）")

    def do_lift(self, context: ContextIF, hour: int) -> None:
        pass

    def __str__(self) -> str:
        return "[昼間]"

    class Config(BaseFrozenConfig):
        pass


class NightState(BaseSingleton, StateIF):
    def do_clock(self, context: ContextIF, hour: int) -> None:
        _switch_context_by_hour(context, hour)

    def do_use(self, context: ContextIF) -> None:
        context.call_security_center("非常：夜間の金庫使用！")

    def do_alarm(self, context: ContextIF) -> None:
        context.call_security_center("非常ベル（夜間）")
        context.change_state(cast(StateIF, UrgentState.get_instance()))

    def do_phone(self, context: ContextIF) -> None:
        context.record_log("夜間の通常録音")

    def do_lift(self, context: ContextIF, hour: int) -> None:
        pass

    def __str__(self) -> str:
        return "[夜間]"

    class Config(BaseFrozenConfig):
        pass


class NoonState(BaseSingleton, StateIF):
    def do_clock(self, context: ContextIF, hour: int) -> None:
        _switch_context_by_hour(context, hour)

    def do_use(self, context: ContextIF) -> None:
        context.call_security_center("非常：昼食時の金庫使用！")

    def do_alarm(self, context: ContextIF) -> None:
        context.call_security_center("非常ベル（昼食時）")
        context.change_state(cast(StateIF, UrgentState.get_instance()))

    def do_phone(self, context: ContextIF) -> None:
        context.record_log("昼食時の通常録音")

    def do_lift(self, context: ContextIF, hour: int) -> None:
        pass

    def __str__(self) -> str:
        return "[昼食時]"

    class Config(BaseFrozenConfig):
        pass


class UrgentState(BaseSingleton, StateIF):
    def do_clock(self, context: ContextIF, hour: int) -> None:
        pass

    def do_use(self, context: ContextIF) -> None:
        context.call_security_center("非常：非常時の金庫使用！")

    def do_alarm(self, context: ContextIF) -> None:
        context.call_security_center("非常ベル（非常時）")

    def do_phone(self, context: ContextIF) -> None:
        context.record_log("非常時の通常録音")

    def do_lift(self, context: ContextIF, hour: int) -> None:
        _switch_context_by_hour(context, hour)

    def __str__(self) -> str:
        return "[非常時]"

    class Config(BaseFrozenConfig):
        pass


DayState()
NightState()
NoonState()
UrgentState()
