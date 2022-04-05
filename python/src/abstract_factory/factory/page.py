import abc
from typing import Any, List

from pydantic import PrivateAttr

from ...common.custom_pydantic.model import ABCModel
from .item import ItemABC

DEFAULT_ENCODING = "utf-8"


class PageABC(ABCModel):
    _title: str = PrivateAttr()
    _author: str = PrivateAttr()
    _content: List[ItemABC] = PrivateAttr(default=[])

    def __init__(self, title: str, author: str, **data: Any) -> None:
        super().__init__(**data)
        self._title = title
        self._author = author

    def add(self, item: ItemABC) -> None:
        self._content.append(item)

    @abc.abstractmethod
    def make_html(self) -> str:
        pass

    def output(self) -> str:
        filename = f"{self._title}.html"
        with open(filename, mode="w", encoding=DEFAULT_ENCODING) as f:
            f.write(self.make_html())
        print(f"{filename}を作成しました")

        return filename
