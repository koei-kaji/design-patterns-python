import abc

from pydantic import BaseModel

from .config import ABCConfig


class ABCModel(BaseModel, abc.ABC):
    class Config(ABCConfig):
        pass
