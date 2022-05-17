import os
import tkinter as tk

import pytest
from pydantic.color import Color

from src.command.color_command import ColorCommand
from src.command.command import CommandIF
from src.command.draw_canvas import DrawCanvas
from src.command.draw_command import DrawCommand
from src.command.macro_command import MacroCommand
from src.command.point import Point


@pytest.mark.skipif(
    condition=(os.environ.get("GITHUB_ACTIONS") == "true"),
    reason="Needs to be interactive.",
)
class TestDrawCanvas:
    root: tk.Tk
    button_frame: tk.Frame
    button_clear: tk.Button
    button_red: tk.Button
    button_green: tk.Button
    button_blue: tk.Button
    button_undo: tk.Button
    history: MacroCommand
    canvas: DrawCanvas

    def _onclick_button_clear(self) -> None:
        self.history.clear()
        self.canvas.delete("all")

    def _onclick_button_color(self, color: Color) -> None:
        command: CommandIF = ColorCommand(drawable=self.canvas, color=color)
        self.history.append(command)
        command.execute()

    def _onclick_button_red(self) -> None:
        self._onclick_button_color(Color("red"))

    def _onclick_button_green(self) -> None:
        self._onclick_button_color(Color("green"))

    def _onclick_button_blue(self) -> None:
        self._onclick_button_color(Color("blue"))

    def _onclick_button_undo(self) -> None:
        self.history.undo()
        self.canvas.delete("all")
        self.history.execute()

    # NOTE: ??? -> Missing type parameters for generic type "Event"
    def _ondrag_canvas(self, event: tk.Event) -> None:  # type: ignore[type-arg]
        point = Point(x=event.x, y=event.y)
        command: CommandIF = DrawCommand(drawable=self.canvas, position=point)
        self.history.append(command)
        command.execute()

    def test_normal(self) -> None:
        self.root = tk.Tk()
        self.button_frame = tk.Frame(self.root)
        self.button_clear = tk.Button(
            self.button_frame,
            text="Clear",
            anchor=tk.CENTER,
            command=self._onclick_button_clear,
        )
        self.button_red = tk.Button(
            self.button_frame,
            text="Red",
            anchor=tk.CENTER,
            command=self._onclick_button_red,
        )
        self.button_green = tk.Button(
            self.button_frame,
            text="Green",
            anchor=tk.CENTER,
            command=self._onclick_button_green,
        )
        self.button_blue = tk.Button(
            self.button_frame,
            text="Blue",
            anchor=tk.CENTER,
            command=self._onclick_button_blue,
        )
        self.button_undo = tk.Button(
            self.button_frame,
            text="Undo",
            anchor=tk.CENTER,
            command=self._onclick_button_undo,
        )
        self.history = MacroCommand()
        self.canvas = DrawCanvas(400, 400, self.history, self.root)
        self.canvas.bind("<B1-Motion>", self._ondrag_canvas)
        self.button_frame.grid(row=0, column=0)
        self.button_clear.grid(row=0, column=0)
        self.button_red.grid(row=0, column=1)
        self.button_green.grid(row=0, column=2)
        self.button_blue.grid(row=0, column=3)
        self.button_undo.grid(row=0, column=4)
        self.canvas.grid(row=1, column=0, sticky=tk.NSEW)

        self.root.after(3000, self.root.destroy)
        self.root.mainloop()
