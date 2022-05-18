from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .exc import InstantiationError


class BaseSingleton(BaseModel):
    def __new__(cls) -> BaseSingleton:
        if hasattr(cls, "_singleton"):
            raise InstantiationError("This singleton has been already created")
        cls._singleton: BaseSingleton = super().__new__(cls)
        return cls._singleton

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        print("インスタンスを生成しました")

    @classmethod
    def get_instance(cls) -> BaseSingleton:
        return cls._singleton
