from pydantic import BaseModel, StrictInt

from ..common.custom_pydantic.config import BaseConfig


class Point(BaseModel):
    x: StrictInt
    y: StrictInt

    class Config(BaseConfig):
        pass
