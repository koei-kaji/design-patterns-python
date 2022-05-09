from ..common.custom_pydantic.config import BaseFrozenConfig
from .support import SupportABC
from .trouble import Trouble


class NoSupport(SupportABC):
    def _resolve(self, trouble: Trouble) -> bool:
        return False

    class Config(SupportABC.Config, BaseFrozenConfig):
        pass
