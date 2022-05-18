import tkinter as tk
from enum import Enum
from typing import Final

from .colleague_button import ColleagueButton
from .colleague_entry import ColleagueEntry
from .colleague_radio_button import ColleagueRadioButton
from .mediator import MediatorIF


class LoginFrame(tk.Frame, MediatorIF):
    check_label_frame: tk.LabelFrame
    check_radio_guest: ColleagueRadioButton
    check_radio_login: ColleagueRadioButton
    check_var: tk.StringVar
    user_label_username: tk.Label
    user_label_password: tk.Label
    user_entry_username: ColleagueEntry
    user_entry_password: ColleagueEntry
    run_frame: tk.Frame
    run_button_ok: ColleagueButton
    run_button_cancel: ColleagueButton
    MIN_LIMIT_USERNAME: Final[int] = 4
    MIN_LIMIT_PASSWORD: Final[int] = 4

    class Account(Enum):
        GUEST = "guest"
        LOGIN = "login"

    def __init__(self, master=None, cnf=None, **kw) -> None:  # type: ignore[no-untyped-def]
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)

        # 生成
        self.create_colleagues()

        # 配置
        self.check_label_frame.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E)
        self.check_radio_guest.grid(row=0, column=0)
        self.check_radio_login.grid(row=0, column=1)
        self.user_label_username.grid(row=1, column=0, sticky=tk.W)
        self.user_entry_username.grid(row=1, column=1)
        self.user_label_password.grid(row=2, column=0, sticky=tk.W)
        self.user_entry_password.grid(row=2, column=1)
        self.run_frame.grid(row=3, column=1, sticky=tk.E)
        self.run_button_ok.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.run_button_cancel.grid(row=0, column=1, sticky=tk.W + tk.E)

        # 有効/無効の初期指定
        self.colleague_changed()

    def create_colleagues(self) -> None:
        # Account(guest, login)
        self.check_label_frame = tk.LabelFrame(self, text="Account", padx=10, pady=10)
        self.check_var = tk.StringVar()
        self.check_radio_guest = ColleagueRadioButton(
            self.check_label_frame,
            text="Guest",
            value=self.Account.GUEST.value,
            variable=self.check_var,
        )
        self.check_radio_login = ColleagueRadioButton(
            self.check_label_frame,
            text="Login",
            value=self.Account.LOGIN.value,
            variable=self.check_var,
        )

        # username, password
        self.user_label_username = tk.Label(self, text="Username:", padx=5, pady=2)
        self.user_label_password = tk.Label(self, text="Password:", padx=5, pady=2)
        self.user_entry_username = ColleagueEntry(self, width=20)
        self.user_entry_password = ColleagueEntry(self, width=20)

        # ok, cancel
        self.run_frame = tk.Frame(self, padx=2, pady=2)
        self.run_button_ok = ColleagueButton(
            self.run_frame, text="OK", command=self.master.quit
        )
        self.run_button_cancel = ColleagueButton(
            self.run_frame, text="Cancel", command=self.master.quit
        )

        self.check_radio_guest.set_mediator(self)
        self.check_radio_login.set_mediator(self)
        self.user_entry_username.set_mediator(self)
        self.user_entry_password.set_mediator(self)
        self.run_button_ok.set_mediator(self)
        self.run_button_cancel.set_mediator(self)

    def colleague_changed(self) -> None:
        if self.check_var.get() == self.Account.GUEST.value:
            self.user_entry_username.set_colleague_enabled(False)
            self.user_entry_password.set_colleague_enabled(False)
            self.run_button_ok.set_colleague_enabled(True)
        else:
            self.user_entry_username.set_colleague_enabled(True)
            self._user_changed()

    def _user_changed(self) -> None:
        if self.user_entry_username.get():
            self.user_entry_password.set_colleague_enabled(True)
            if (len(self.user_entry_username.get()) >= self.MIN_LIMIT_USERNAME) and (
                len(self.user_entry_password.get()) >= self.MIN_LIMIT_PASSWORD
            ):
                self.run_button_ok.set_colleague_enabled(True)
            else:
                self.run_button_ok.set_colleague_enabled(False)
        else:
            self.user_entry_password.set_colleague_enabled(False)
            self.run_button_ok.set_colleague_enabled(False)
