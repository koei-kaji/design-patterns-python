from __future__ import annotations

from time import sleep
from typing import Any, Optional

from pydantic import BaseModel, PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .printable import PrintableIF


class Printer(BaseModel, PrintableIF):
    _name: Optional[str] = PrivateAttr()

    def __init__(self, name: Optional[str] = None, **data: Any) -> None:
        super().__init__(**data)
        self._name = name
        self._heavy_job("Printerのインスタンスを生成中")

    def set_printer_name(self, name: str) -> None:
        self._name = name

    def get_printer_name(self) -> str:
        return str(self._name)

    def print(self, string: str) -> None:
        print(f"==={self._name}===")
        print(string)

    def _heavy_job(self, message: str) -> None:
        print(message, end="", flush=True)
        for _ in range(5):
            sleep(0.2)
            print(".", end="", flush=True)
        print("完了", flush=True)

    class Config(BaseFrozenConfig):
        pass
