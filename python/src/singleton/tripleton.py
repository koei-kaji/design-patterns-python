from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel, PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .exc import InstantiationError


class _Tripleton(BaseModel):
    _id: int = PrivateAttr()
    _tripleton: List[_Tripleton] = []

    def __new__(cls, _id: int, **_: Any) -> _Tripleton:
        if len(cls._tripleton) >= 3:
            raise InstantiationError(
                "Instance of this class has been already created three times"
            )
        cls._tripleton.append(super().__new__(cls))
        return cls._tripleton[-1]

    def __init__(self, _id: int, **data: Any) -> None:
        super().__init__(**data)
        self._id = _id
        print(f"The instance id={self._id}({id(self._tripleton[-1])}) is created")

    def get_instance(self, _id: int) -> _Tripleton:
        print(self._tripleton[_id])
        return self._tripleton[_id]

    def __str__(self) -> str:
        return f"[Triple id={self._id}({id(self)})]"

    class Config(BaseFrozenConfig):
        pass


Tripleton = [_Tripleton(_id=i) for i in range(3)][0]
