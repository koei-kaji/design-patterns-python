from typing import Any, List

from pydantic import BaseModel, PrivateAttr

from .big_char import BigChar
from .big_char_factory import BigCharFactory


class BigString(BaseModel):
    _big_chars: List[BigChar] = PrivateAttr(default=[])

    def __init__(self, string: str, is_shared: bool = True, **data: Any) -> None:
        super().__init__(**data)
        if is_shared:
            factory = BigCharFactory
            for char in string:
                self._big_chars.append(factory.get_big_char(char))
        else:
            for char in string:
                self._big_chars.append(BigChar(char=char))

    def print(self) -> None:
        for i in self._big_chars:
            i.print()
