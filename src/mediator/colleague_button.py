import tkinter

from src.mediator.mediator import MediatorIF

from .colleague import ColleagueIF


class ColleagueButton(tkinter.Button, ColleagueIF):
    _mediator: MediatorIF

    def set_mediator(self, mediator: MediatorIF) -> None:
        self._mediator = mediator

    def set_colleague_enabled(self, enabled: bool) -> None:
        self["state"] = tkinter.NORMAL if enabled else tkinter.DISABLED
