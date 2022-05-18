import os
import random
import threading
from time import sleep

import pytest

from src.state.safe_tk import SafeTk


@pytest.mark.skipif(
    condition=(os.environ.get("GITHUB_ACTIONS") == "true"),
    reason="Needs to be interactive.",
)
class TestSafeTk:
    root: SafeTk

    def process(self) -> None:
        # pylint: disable=protected-access
        callbacks_non_urgent = [
            self.root._callback_use,
            self.root._callback_alarm,
            self.root._callback_phone,
        ]
        callbacks_urgent = [
            self.root._callback_use,
            self.root._callback_phone,
            self.root._callback_lift,
        ]
        # pylint: enable=protected-access
        is_urgent: bool = False

        for hour in range(24):
            self.root.set_clock(hour)

            for _ in range(3):
                if is_urgent:
                    callback = random.choice(callbacks_urgent)
                else:
                    callback = random.choice(callbacks_non_urgent)

                callback()
                # pylint: disable=protected-access
                if (
                    callback.__func__  # type: ignore[attr-defined]
                    is self.root._callback_alarm.__func__  # type: ignore[attr-defined]
                ) or (
                    callback.__func__ is self.root._callback_lift.__func__  # type: ignore[attr-defined]
                ):
                    is_urgent = not is_urgent
                # pylint: enable=protected-access

            sleep(0.05)

    def test_normal(self) -> None:
        self.root = SafeTk()

        # NOTE: tkinterはメインスレッドにするのが妥当らしい
        thread = threading.Thread(target=self.process)
        thread.start()

        self.root.after(4000, self.root.destroy)
        self.root.mainloop()
