from __future__ import annotations

import tkinter as tk
from typing import Any, Callable, Optional, TypeVar

from src.state.state import DayState, StateIF, UrgentState

from .context import ContextIF


class SafeTk(tk.Tk, ContextIF):
    _state: StateIF
    _clock_label: tk.Label
    _clock_var: tk.StringVar
    _clock_hour: int
    _security_center_frame: tk.Frame
    _security_center_text: tk.Text
    _security_center_scrollbar: tk.Scrollbar

    _button_frame: tk.Frame
    _button_use: tk.Button
    _button_alarm: tk.Button
    _button_phone: tk.Button
    _button_lift: tk.Button
    _button_exit: tk.Button

    def __init__(
        self,
        screenName: Optional[str] = None,
        baseName: Optional[str] = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: Optional[str] = None,
    ):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self._state = DayState
        self._clock_var = tk.StringVar()
        self._clock_label = tk.Label(
            self, textvariable=self._clock_var, width=30, anchor=tk.W
        )
        self._security_center_frame = tk.Frame(self)
        self._security_center_text = tk.Text(
            self._security_center_frame, width=50, height=20
        )
        self._security_center_scrollbar = tk.Scrollbar(
            self._security_center_frame,
            orient=tk.VERTICAL,
            command=self._security_center_text.yview,
        )
        self._security_center_text[
            "yscrollcommand"
        ] = self._security_center_scrollbar.set
        self._button_frame = tk.Frame(self)
        self._button_use = tk.Button(
            self._button_frame, text="金庫使用", command=self._callback_use
        )
        self._button_alarm = tk.Button(
            self._button_frame, text="非常ベル", command=self._callback_alarm
        )
        self._button_phone = tk.Button(
            self._button_frame, text="通常通話", command=self._callback_phone
        )
        self._button_lift = tk.Button(
            self._button_frame,
            text="解除",
            command=self._callback_lift,
            state=tk.DISABLED,
        )
        self._button_exit = tk.Button(
            self._button_frame, text="終了", command=self.destroy
        )

        self._clock_label.grid(row=0, column=0, sticky=tk.EW)
        self._security_center_frame.grid(row=1, column=0)
        self._security_center_text.grid(row=0, column=0, sticky=tk.NSEW)
        self._security_center_scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self._button_frame.grid(row=2, column=0, sticky=tk.E)
        self._button_use.grid(row=0, column=0)
        self._button_alarm.grid(row=0, column=1)
        self._button_phone.grid(row=0, column=2)
        self._button_lift.grid(row=0, column=3)
        self._button_exit.grid(row=0, column=4)

    def _callback_use(self) -> None:
        self._state.do_use(self)

    def _callback_alarm(self) -> None:
        self._state.do_alarm(self)
        self._button_lift.configure(state=tk.NORMAL)
        self._button_alarm.configure(state=tk.DISABLED)

    def _callback_phone(self) -> None:
        self._state.do_phone(self)

    def _callback_lift(self) -> None:
        self._state.do_lift(self, self._clock_hour)
        self._button_lift.configure(state=tk.DISABLED)
        self._button_alarm.configure(state=tk.NORMAL)

    def set_clock(self, hour: int) -> None:
        str_clock = f"現在時刻は{str(hour).zfill(2)}:00"
        print(str_clock)
        self._clock_var.set(str_clock)
        self._state.do_clock(self, hour)
        self._clock_hour = hour

    # TODO: pylint, mypyコメントだらけをどうにかしたい
    # NOTE: https://github.com/python/mypy/issues/7778
    R = TypeVar("R")
    # pylint: disable=no-self-argument
    def moveto_bottom(func: Callable[..., R]) -> Callable[..., R]:  # type: ignore[misc]
        def inner(self: SafeTk, *args: Any, **kwargs: Any) -> Any:
            # pylint: disable=not-callable
            func(self, *args, **kwargs)
            # pylint: enable=not-callable
            # pylint: disable=protected-access
            self._security_center_text.yview_moveto(1.0)
            # pylint: enable=protected-access

        return inner

    # pylint: enable=no-self-argument

    @moveto_bottom
    def change_state(self, state: StateIF) -> None:
        if self._state is UrgentState:
            print("非常時が解除されました")
        if type(state) is not type(self._state):
            print(f"{self._state}から{state}へ状態が変化しました")
        self._state = state

    @moveto_bottom
    def call_security_center(self, message: str) -> None:
        self._security_center_text.insert(tk.END, f"call! {message}\n")

    @moveto_bottom
    def record_log(self, message: str) -> None:
        self._security_center_text.insert(tk.END, f"record... {message}\n")
