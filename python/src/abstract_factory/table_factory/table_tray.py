from typing import Any, List

from ..factory.tray import TrayABC


class TableTray(TrayABC):
    def __init__(self, caption: str, **data: Any) -> None:
        super().__init__(caption=caption, **data)

    def make_html(self) -> str:
        buffer: List[str] = [
            "<td>",
            '<table width="100%" border="1"><tr>',
            f'<td bgcolor="#cccccc" align="center" colspan="{len(self._tray)}"><b>{self._caption}</b></td>',
            "</tr>",
            "<tr>",
            *[item.make_html() for item in self._tray],
            "</tr></table>",
            "</td>",
        ]

        return "\n".join(buffer)
