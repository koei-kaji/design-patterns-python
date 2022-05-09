from __future__ import annotations

import abc
from typing import Optional, final

from pydantic import PrivateAttr

from ..common.custom_pydantic.model import ABCModel
from .trouble import Trouble


class SupportABC(ABCModel):
    name: str
    _next: Optional[SupportABC] = PrivateAttr(default=None)

    def set_next(self, __next: SupportABC) -> SupportABC:
        self._next = __next
        return __next

    @abc.abstractmethod
    def _resolve(self, trouble: Trouble) -> bool:
        pass

    def _done(self, trouble: Trouble) -> None:
        print(f"{trouble} is resolved by {self}.")

    def _fail(self, trouble: Trouble) -> None:
        print(f"{trouble} cannot be resolved.")

    @final
    def support(self, trouble: Trouble, exec_recursively: bool = True) -> None:
        # pylint: disable=protected-access
        if exec_recursively:
            if self._resolve(trouble):
                self._done(trouble)
            elif self._next is not None:
                self._next.support(trouble)
            else:
                self._fail(trouble)
        else:
            spt: SupportABC = self
            while True:
                if spt._resolve(trouble):
                    spt._done(trouble)
                    break
                elif spt._next is None:
                    spt._fail(trouble)
                    break
                else:
                    spt = spt._next

    def __str__(self) -> str:
        return f"[{self.name}]"
