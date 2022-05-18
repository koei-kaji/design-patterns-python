import tkinter

from src.mediator.mediator import MediatorIF

from .colleague import ColleagueIF


class ColleagueEntry(tkinter.Entry, ColleagueIF):
    _mediator: MediatorIF
    sv: tkinter.StringVar

    # pylint: disable=dangerous-default-value
    def __init__(self, master=None, cnf={}, **kw) -> None:  # type: ignore[no-untyped-def]
        super().__init__(master, cnf, **kw)

        # NOTE: https://stackoverflow.com/questions/6548837/how-do-i-get-an-event-callback-when-a-tkinter-entry-widget-is-modified
        sv = tkinter.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self._callback(sv))  # type: ignore[no-untyped-call]
        self["textvariable"] = sv

    # pylint: enable=dangerous-default-value

    def set_mediator(self, mediator: MediatorIF) -> None:
        self._mediator = mediator

    def set_colleague_enabled(self, enabled: bool) -> None:
        self["state"] = tkinter.NORMAL if enabled else tkinter.DISABLED
        # TODO: backgroundcolorの設定いるか要確認

    def _callback(self, _: tkinter.StringVar) -> None:
        self._mediator.colleague_changed()
