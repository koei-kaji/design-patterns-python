from typing import Any

from pydantic import PrivateAttr

from .item import ItemABC


class LinkABC(ItemABC):
    _url: str = PrivateAttr()

    def __init__(self, caption: str, url: str, **data: Any) -> None:
        super().__init__(caption=caption, **data)
        self._url = url
