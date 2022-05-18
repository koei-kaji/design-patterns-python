import tkinter
from typing import Any, List

from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseConfig
from .builder import BuilderABC


class TkBuilder(BuilderABC):
    _tk: tkinter.Tk = PrivateAttr()
    _widgets: List[tkinter.Widget] = PrivateAttr(default=[])

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self._tk = tkinter.Tk()
        self._tk.geometry("300x300")

    def make_title(self, title: str) -> None:
        self._tk.title(title)

    def make_string(self, string: str) -> None:
        self._widgets.append(tkinter.Label(self._tk, text=string))

    def make_items(self, items: List[str]) -> None:
        for item in items:
            self._widgets.append(tkinter.Button(self._tk, text=item))

    def close(self) -> None:
        for widget in self._widgets:
            widget.pack(side="top")

    def get_result(self) -> tkinter.Tk:
        return self._tk

    class Config(BuilderABC.Config, BaseConfig):
        pass
