from pydantic import BaseModel
from pydantic.color import Color

from ..common.custom_pydantic.config import BaseFrozenConfig
from .command import CommandIF
from .drawable import DrawableIF


class ColorCommand(BaseModel, CommandIF):
    drawable: DrawableIF
    color: Color

    def execute(self) -> None:
        self.drawable.set_color(self.color)

    class Config(BaseFrozenConfig):
        arbitrary_types_allowed = True
