from typing import List

from pydantic import PrivateAttr

from .builder import BuilderABC


class TextBuilder(BuilderABC):
    _texts: List[str] = PrivateAttr(default=[])

    def make_title(self, title: str) -> None:
        self._texts.extend(
            [
                "\n",
                "=========================\n",
                f"『{title}』\n",
                "\n",
            ]
        )

    def make_string(self, string: str) -> None:
        self._texts.extend(
            [
                f"■{string}\n",
                "\n",
            ]
        )

    def make_items(self, items: List[str]) -> None:
        self._texts.extend([f" ・{item}\n" for item in items])

    def close(self) -> None:
        self._texts.extend(
            [
                "=========================\n",
            ]
        )

    def get_result(self) -> str:
        return "".join(self._texts)
