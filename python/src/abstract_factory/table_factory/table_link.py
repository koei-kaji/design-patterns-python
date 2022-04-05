from typing import Any

from ..factory.link import LinkABC


class TableLink(LinkABC):
    def __init__(self, caption: str, url: str, **data: Any) -> None:
        super().__init__(caption=caption, url=url, **data)

    def make_html(self) -> str:
        return f'<td><a href="{self._url}">{self._caption}</a></td>'
