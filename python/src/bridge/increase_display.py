from typing import Any

from pydantic import StrictInt

from .count_display import CountDisplay
from .display_impl import DisplayImplABC


class IncreaseDisplay(CountDisplay):
    step: StrictInt

    def __init__(self, impl: DisplayImplABC, **data: Any) -> None:
        super().__init__(impl=impl, **data)

    def display_increasily(self, level: int) -> None:
        count = 0
        for _ in range(level):
            self.display_multi(count * self.step)
            count += 1
