import threading
from typing import Dict, Optional

from pydantic import PrivateAttr

from ..singleton._singleton import BaseSingleton
from .big_char import BigChar


class _BigCharFactory(BaseSingleton):
    _lock = threading.Lock()
    _pool: Dict[str, BigChar] = PrivateAttr(default={})

    def get_big_char(self, char: str) -> BigChar:
        with self._lock:
            big_char: Optional[BigChar] = self._pool.get(char, None)
            if big_char is None:
                big_char = BigChar(char=char)
                self._pool[char] = big_char

            return big_char


BigCharFactory = _BigCharFactory()
