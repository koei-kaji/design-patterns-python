import abc
from typing import Any

from pydantic import PrivateAttr

from ...common.custom_pydantic.model import ABCModel


class ItemABC(ABCModel):
    _caption: str = PrivateAttr()

    def __init__(self, caption: str, **data: Any) -> None:
        super().__init__(**data)
        self._caption = caption

    @abc.abstractmethod
    def make_html(self) -> str:
        pass
