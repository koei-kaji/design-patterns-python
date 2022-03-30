from pydantic import BaseModel

from ..common.custom_pydantic import BaseFrozenConfig


class Book(BaseModel):
    name: str

    class Config(BaseFrozenConfig):
        pass
