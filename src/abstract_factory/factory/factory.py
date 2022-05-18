from __future__ import annotations

import abc
import sys
from typing import Callable, cast

from ...common.custom_pydantic.model import ABCModel
from ...common.util import Class_, ClassNotFoundException
from ..factory.link import LinkABC
from ..factory.page import PageABC
from ..factory.tray import TrayABC


class FactoryABC(ABCModel):
    @staticmethod
    def get_factory(class_name: str) -> FactoryABC:
        Factory: Callable[[], FactoryABC]

        try:
            Factory = cast(Callable[[], FactoryABC], Class_.get_class(class_name))
        except ClassNotFoundException:
            print(f"クラス {class_name} が見つかりません", file=sys.stderr)
            raise
        else:
            return Factory()

    @abc.abstractmethod
    def create_link(self, caption: str, url: str) -> LinkABC:
        pass

    @abc.abstractmethod
    def create_tray(self, caption: str) -> TrayABC:
        pass

    @abc.abstractmethod
    def create_page(self, title: str, author: str) -> PageABC:
        pass

    def create_yahoo_page(self) -> PageABC:
        link = self.create_link("Yahoo!", "http://www.yahoo.com/")
        page = self.create_page("Yahoo!", "Yahoo!")
        page.add(link)

        return page
