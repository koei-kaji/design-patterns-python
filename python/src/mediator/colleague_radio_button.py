import tkinter

from src.mediator.mediator import MediatorIF

from .colleague import ColleagueIF


class ColleagueRadioButton(tkinter.Radiobutton, ColleagueIF):
    _mediator: MediatorIF
    _value: tkinter.IntVar

    # pylint: disable=dangerous-default-value
    def __init__(self, master=None, cnf={}, **kw) -> None:  # type: ignore[no-untyped-def]
        super().__init__(master, cnf, **kw)
        self["command"] = self._selected

    # pylint: enable=dangerous-default-value

    def set_mediator(self, mediator: MediatorIF) -> None:
        self._mediator = mediator

    def set_colleague_enabled(self, enabled: bool) -> None:
        self["state"] = tkinter.NORMAL if enabled else tkinter.DISABLED

    def _selected(self) -> None:
        self._mediator.colleague_changed()
