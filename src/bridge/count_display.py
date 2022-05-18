from typing import Any

from .display import Display
from .display_impl import DisplayImplABC


class CountDisplay(Display):
    def __init__(self, impl: DisplayImplABC, **data: Any) -> None:
        super().__init__(impl=impl, **data)

    def display_multi(self, times: int) -> None:
        self.open()
        for _ in range(times):
            self.print()
        self.close()
