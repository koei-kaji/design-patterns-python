from io import FileIO

from pydantic import BaseModel

from ...common.custom_pydantic.config import BaseFrozenConfig


class HtmlWriter(BaseModel):
    writer: FileIO

    def _write(self, string: str) -> None:
        self.writer.write(string.encode())

    def title(self, title: str) -> None:
        self._write("<html>")
        self._write("<head>")
        self._write(f"<title>{title}</title>")
        self._write("</head>")
        self._write("<body>\n")
        self._write(f"<h1>{title}</h1>\n")

    def paragraph(self, message: str) -> None:
        self._write(f"<p>{message}</p>\n")

    def link(self, href: str, caption: str) -> None:
        self.paragraph(f'<a href="{href}">{caption}</a>')

    def mailto(self, mail_address: str, user_name: str) -> None:
        self.link(f"mailto:{mail_address}", user_name)

    def close(self) -> None:
        self._write("</body>")
        self._write("</html>\n")
        self.writer.close()

    class Config(BaseFrozenConfig):
        arbitrary_types_allowed = True
