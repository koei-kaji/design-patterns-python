from ..common.custom_pydantic.config import BaseFrozenConfig
from ._singleton import BaseSingleton


class _Singleton(BaseSingleton):
    class Config(BaseFrozenConfig):
        pass


Singleton = _Singleton()
