import threading
from typing import Dict, Optional

from pydantic import PrivateAttr

from ..common.decorator import synchronized
from ..singleton._singleton import BaseSingleton
from .big_char import BigChar


class BigCharFactory(BaseSingleton):
    _lock = threading.Lock()
    _pool: Dict[str, BigChar] = PrivateAttr(default={})

    @synchronized(_lock)
    def get_big_char(self, char: str) -> BigChar:
        big_char: Optional[BigChar] = self._pool.get(char, None)
        if big_char is None:
            big_char = BigChar(char=char)
            self._pool[char] = big_char

        return big_char


BigCharFactory()
