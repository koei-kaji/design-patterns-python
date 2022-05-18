import os
import tkinter as tk

import pytest

from src.mediator.login_frame import LoginFrame


class TestLoginFrame:
    @pytest.mark.skipif(
        condition=(os.environ.get("GITHUB_ACTIONS") == "true"),
        reason="Needs to be interactive.",
    )
    def test_normal(self) -> None:
        root = tk.Tk()
        frame = LoginFrame(root)
        frame.pack()

        # NOTE: テストは面倒なのでとりあえず描画
        root.after(3000, root.destroy)
        root.mainloop()
