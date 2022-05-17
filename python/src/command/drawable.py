import abc

from pydantic.color import Color

from ..common.model import Interface


class DrawableIF(Interface):
    @abc.abstractmethod
    def draw(self, x: int, y: int) -> None:
        pass

    @abc.abstractmethod
    def set_color(self, color: Color) -> None:
        pass
