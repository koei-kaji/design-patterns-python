from pydantic import BaseModel

from ..common.custom_pydantic.config import BaseFrozenConfig


class Book(BaseModel):
    name: str

    class Config(BaseFrozenConfig):
        pass
