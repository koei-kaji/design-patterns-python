from pydantic import StrictInt, StrictStr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .entry import EntryABC


class File(EntryABC):
    name: StrictStr
    size: StrictInt

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def _print_list(self, prefix: str) -> None:
        print(f"{prefix}/{self}")

    class Config(EntryABC.Config, BaseFrozenConfig):
        pass
