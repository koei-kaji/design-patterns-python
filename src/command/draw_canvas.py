import tkinter as tk
from typing import Any, Dict, Optional

from pydantic.color import Color

from .color_command import ColorCommand
from .drawable import DrawableIF
from .macro_command import MacroCommand


class DrawCanvas(tk.Canvas, DrawableIF):
    _color: Color = Color("red")
    _radius: int = 6
    _history: MacroCommand

    def __init__(
        self,
        width: int,
        height: int,
        history: MacroCommand,
        master: Optional[tk.Misc] = None,
        cnf: Optional[Dict[str, Any]] = None,
        **kw: Any
    ) -> None:

        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, bg="white", width=width, height=height, **kw)
        self._history = history
        self._history.append(ColorCommand(drawable=self, color=self._color))

    def paint(self) -> None:
        self._history.execute()

    def draw(self, x: float, y: float) -> None:
        x1, y1 = (x - self._radius), (y - self._radius)
        x2, y2 = (x + self._radius), (y + self._radius)
        self.create_oval(
            x1, y1, x2, y2, fill=self._color.as_hex(), outline=self._color.as_hex()
        )

    def set_color(self, color: Color) -> None:
        self._color = color
