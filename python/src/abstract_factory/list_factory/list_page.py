from typing import Any, List

from ..factory.page import PageABC


class ListPage(PageABC):
    def __init__(self, title: str, author: str, **data: Any) -> None:
        super().__init__(title=title, author=author, **data)

    def make_html(self) -> str:
        buffer: List[str] = [
            f"<html><head><title>{self._title}</title></head>",
            "<body>",
            f"<h1>{self._title}</h1>",
            "<ul>",
            *[item.make_html() for item in self._content],
            "</ul>",
            f"<hr><address>{self._author}</address>",
            "</body></html>",
        ]

        return "\n".join(buffer)
