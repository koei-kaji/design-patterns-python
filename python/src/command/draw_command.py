from pydantic import BaseModel

from ..common.custom_pydantic.config import BaseFrozenConfig
from .command import CommandIF
from .drawable import DrawableIF
from .point import Point


class DrawCommand(BaseModel, CommandIF):
    drawable: DrawableIF
    position: Point

    def execute(self) -> None:
        self.drawable.draw(self.position.x, self.position.y)

    class Config(BaseFrozenConfig):
        arbitrary_types_allowed = True
