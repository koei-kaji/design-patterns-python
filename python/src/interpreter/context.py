import tokenize
from io import StringIO
from typing import Any, Generator, Optional

from pydantic import BaseModel, PrivateAttr

from .exc import ParseException


class Context(BaseModel):
    _tokens: Generator[tokenize.TokenInfo, None, None] = PrivateAttr()
    _current_token: Optional[str] = PrivateAttr()

    def __init__(self, text: str, **data: Any) -> None:
        super().__init__(**data)
        self._tokens = tokenize.generate_tokens(StringIO(text).readline)
        self.next_token()

    def next_token(self) -> Optional[str]:
        try:
            current_token_info = self._tokens.__next__()
            self._current_token = current_token_info.string
        except StopIteration:
            print("HRERER")
            self._current_token = None

        return self._current_token

    def current_token(self) -> Optional[str]:
        return self._current_token

    def skip_token(self, token: str) -> None:
        if token != self._current_token:
            raise ParseException(
                f"Warning: {token} is expected, but {self._current_token} is found."
            )
        self.next_token()

    def current_number(self) -> int:
        if self._current_token is None:
            raise ParseException(f"Warning: current token is {self._current_token}.")

        try:
            number = int(self._current_token)
        except (ValueError) as error:
            raise ParseException(f"Warning: {error}") from error
        else:
            return number
