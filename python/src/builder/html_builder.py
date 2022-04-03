from typing import List

from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseConfig
from .builder import BuilderABC

DEFAULT_ENCODING = "utf-8"


class HTMLBuilder(BuilderABC):
    _filename: str = PrivateAttr()

    def make_title(self, title: str) -> None:
        self._filename = f"{title}.html"
        with open(self._filename, mode="w", encoding=DEFAULT_ENCODING) as f:
            f.write(f"<html><head><title>{title}</title></head><body>\n")
            f.write(f"<h1>{title}</h1>\n")

    def make_string(self, string: str) -> None:
        with open(self._filename, mode="a", encoding=DEFAULT_ENCODING) as f:
            f.write(f"<p>{string}</p>\n")

    def make_items(self, items: List[str]) -> None:
        with open(self._filename, mode="a", encoding=DEFAULT_ENCODING) as f:
            f.write("<ul>\n")
            for item in items:
                f.write(f"<li>{item}</li>\n")
            f.write("</ul>\n")

    def close(self) -> None:
        with open(self._filename, mode="a", encoding=DEFAULT_ENCODING) as f:
            f.write("</body></html>\n")

    def get_result(self) -> str:
        return self._filename

    class Config(BuilderABC.Config, BaseConfig):
        pass
