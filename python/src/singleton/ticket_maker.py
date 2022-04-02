from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseConfig
from ._singleton import BaseSingleton


class _TicketMaker(BaseSingleton):
    _ticket: int = PrivateAttr(default=1000)

    def get_next_ticket_number(self) -> int:
        ticket_number = self._ticket
        self._ticket += 1
        return ticket_number

    class Config(BaseConfig):
        pass


TicketMaker = _TicketMaker()
