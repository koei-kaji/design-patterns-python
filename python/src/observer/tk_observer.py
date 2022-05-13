from __future__ import annotations

import tkinter as tk
from time import sleep
from typing import List, Optional

import numpy as np
from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from .number_generator import NumberGeneratorABC
from .observer import ObserverIF


class TkObserver(tk.Tk, ObserverIF):
    _text_label: _LabelObserver
    _close_button: tk.Button
    _graph_frame: _GraphObserver

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

        self._text_label = _LabelObserver(self, width=50, anchor=tk.W)
        self._graph_frame = _GraphObserver(self)
        self._close_button = tk.Button(self, text="Close", command=self.destroy)

        self._text_label.grid(row=0, column=0, sticky=tk.EW)
        self._graph_frame.grid(row=1, column=0, sticky=tk.EW)
        self._close_button.grid(row=2, column=0, sticky=tk.EW)

    def subscribe(self, generator: NumberGeneratorABC) -> None:
        self._text_label.subscribe(generator)
        self._graph_frame.subscribe(generator)
        sleep(0.1)


class _LabelObserver(tk.Label, ObserverIF):
    _var: tk.StringVar

    def __init__(self, master=None, cnf=None, **kw) -> None:  # type: ignore[no-untyped-def]
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)
        self._var = tk.StringVar()
        self["textvariable"] = self._var

    def subscribe(self, generator: NumberGeneratorABC) -> None:
        number = generator.get_number()
        self._var.set(f"{number}:{'*' * number}")


class _GraphObserver(tk.Frame, ObserverIF):
    _figure: Figure = Figure(figsize=(5, 4), dpi=100)
    _axes: Axes
    _numbers: List[int] = []

    def __init__(self, master=None, cnf=None, **kw) -> None:  # type: ignore[no-untyped-def]
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)
        self._clear()
        self.figure_canvas = FigureCanvasTkAgg(self._figure, self)
        self.figure_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _clear(self) -> None:
        self._figure.clear()
        self._axes = self._figure.add_subplot(111)

    def subscribe(self, generator: NumberGeneratorABC) -> None:
        self._numbers.append(generator.get_number())
        self._clear()
        self._axes.bar(np.arange(len(self._numbers)), self._numbers)
        self.figure_canvas.draw_idle()
