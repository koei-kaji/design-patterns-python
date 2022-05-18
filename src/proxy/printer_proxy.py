import threading
from typing import Any, Optional

from pydantic import BaseModel, PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .printable import PrintableIF
from .printer import Printer


class PrinterProxy(BaseModel, PrintableIF):
    _name: Optional[str] = PrivateAttr()
    _real: Optional[Printer] = PrivateAttr(default=None)
    _lock: threading.Lock = PrivateAttr(default_factory=threading.Lock)

    def __init__(self, name: str, **data: Any) -> None:
        super().__init__(**data)
        self._name = name

    def set_printer_name(self, name: str) -> None:
        with self._lock:
            if self._real is not None:
                self._real.set_printer_name(name)
            self._name = name

    def get_printer_name(self) -> str:
        return str(self._name)

    def print(self, string: str) -> None:
        self._realize()
        if self._real is not None:
            self._real.print(string)
        else:
            raise Exception("!?!?!?")

    def _realize(self) -> None:
        with self._lock:
            if self._real is None:
                self._real = Printer(name=self._name)

    class Config(BaseFrozenConfig):
        pass
