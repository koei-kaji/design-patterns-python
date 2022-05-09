from ..common.custom_pydantic.config import BaseFrozenConfig
from .support import SupportABC
from .trouble import Trouble


class SpecialSupport(SupportABC):
    number: int

    def _resolve(self, trouble: Trouble) -> bool:
        if trouble.number == self.number:
            return True
        else:
            return False

    class Config(SupportABC.Config, BaseFrozenConfig):
        pass
