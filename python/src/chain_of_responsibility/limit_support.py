from ..common.custom_pydantic.config import BaseFrozenConfig
from .support import SupportABC
from .trouble import Trouble


class LimitSupport(SupportABC):
    limit: int

    def _resolve(self, trouble: Trouble) -> bool:
        if trouble.number < self.limit:
            return True
        else:
            return False

    class Config(SupportABC.Config, BaseFrozenConfig):
        pass
