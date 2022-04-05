from typing import Any, List

from pydantic import PrivateAttr

from .item import ItemABC


class TrayABC(ItemABC):
    _tray: List[ItemABC] = PrivateAttr(default=[])

    def __init__(self, caption: str, **data: Any) -> None:
        super().__init__(caption=caption, **data)

    def add(self, item: ItemABC) -> None:
        self._tray.append(item)
