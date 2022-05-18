from ..common.custom_pydantic.config import BaseFrozenConfig
from ._singleton import BaseSingleton


class Singleton(BaseSingleton):
    class Config(BaseFrozenConfig):
        pass


Singleton()
