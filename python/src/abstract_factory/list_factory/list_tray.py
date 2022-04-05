from typing import Any, List

from ..factory.tray import TrayABC


class ListTray(TrayABC):
    def __init__(self, caption: str, **data: Any) -> None:
        super().__init__(caption=caption, **data)

    def make_html(self) -> str:
        buffer: List[str] = [
            "<li>",
            self._caption,
            "<ul>",
            *[item.make_html() for item in self._tray],
            "</ul>",
            "</li>",
        ]

        return "\n".join(buffer)
