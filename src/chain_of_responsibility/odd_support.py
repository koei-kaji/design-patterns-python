from ..common.custom_pydantic.config import BaseFrozenConfig
from .support import SupportABC
from .trouble import Trouble


class OddSupport(SupportABC):
    def _resolve(self, trouble: Trouble) -> bool:
        if trouble.number % 2 == 1:
            return True
        else:
            return False

    class Config(SupportABC.Config, BaseFrozenConfig):
        pass
