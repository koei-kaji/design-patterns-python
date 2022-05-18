from pydantic import BaseModel

from ..common.custom_pydantic.config import BaseFrozenConfig


class Trouble(BaseModel):
    number: int

    def __str__(self) -> str:
        return f"[Trouble {self.number}]"

    class Config(BaseFrozenConfig):
        pass
