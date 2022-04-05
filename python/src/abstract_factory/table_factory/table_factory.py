from ..factory.factory import FactoryABC
from ..factory.link import LinkABC
from ..factory.page import PageABC
from ..factory.tray import TrayABC
from ..table_factory.table_link import TableLink
from ..table_factory.table_page import TablePage
from ..table_factory.table_tray import TableTray


class TableFactory(FactoryABC):
    def create_link(self, caption: str, url: str) -> LinkABC:
        return TableLink(caption=caption, url=url)

    def create_tray(self, caption: str) -> TrayABC:
        return TableTray(caption=caption)

    def create_page(self, title: str, author: str) -> PageABC:
        return TablePage(title=title, author=author)
