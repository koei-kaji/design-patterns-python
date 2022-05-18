from ..factory.factory import FactoryABC
from ..factory.link import LinkABC
from ..factory.page import PageABC
from ..factory.tray import TrayABC
from ..list_factory.list_link import ListLink
from ..list_factory.list_page import ListPage
from ..list_factory.list_tray import ListTray


class ListFactory(FactoryABC):
    def create_link(self, caption: str, url: str) -> LinkABC:
        return ListLink(caption=caption, url=url)

    def create_tray(self, caption: str) -> TrayABC:
        return ListTray(caption=caption)

    def create_page(self, title: str, author: str) -> PageABC:
        return ListPage(title=title, author=author)
