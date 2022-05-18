from typing import cast

import pytest

from src.singleton.exc import InstantiationError
from src.singleton.singleton import Singleton
from src.singleton.ticket_maker import TicketMaker
from src.singleton.tripleton import Tripleton


class TestBaseSingleton:
    def test_normal(self) -> None:

        assert Singleton.get_instance() == Singleton.get_instance()

    def test_exc_instantiation_error(self) -> None:

        with pytest.raises(InstantiationError):
            Singleton()


class TestTicketMaker:
    def test_normal(self) -> None:

        DEFAULT_TICKET_NUMBER = 1000
        assert TicketMaker.get_instance() == TicketMaker.get_instance()

        ticket_maker = cast(TicketMaker, TicketMaker.get_instance())
        assert ticket_maker.get_next_ticket_number() == DEFAULT_TICKET_NUMBER + 0
        assert ticket_maker.get_next_ticket_number() == DEFAULT_TICKET_NUMBER + 1


class TestTripleton:
    def test_normal(self) -> None:

        assert Tripleton.get_instance(0) == Tripleton.get_instance(0)
        assert Tripleton.get_instance(1) == Tripleton.get_instance(1)
        assert Tripleton.get_instance(2) == Tripleton.get_instance(2)
        # pylint: disable=protected-access
        assert Tripleton.get_instance(0)._id == 0
        assert Tripleton.get_instance(1)._id == 1
        assert Tripleton.get_instance(2)._id == 2
        # pylint: enable=protected-access

    def test_exc_instantiation_error(self) -> None:
        with pytest.raises(InstantiationError):
            Tripleton(_id=3)
