import random
from typing import Any

from .count_display import CountDisplay
from .display_impl import DisplayImplABC


class RandomCountDisplay(CountDisplay):
    def __init__(self, impl: DisplayImplABC, **data: Any) -> None:
        super().__init__(impl=impl, **data)

    def display_multi_random(self, max_times: int) -> None:
        self.open()
        for _ in range(random.randint(0, max_times)):
            self.print()
        self.close()
