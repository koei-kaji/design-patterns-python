import pytest
from pytest import CaptureFixture

from src.singleton.exc import InstantiationError
from tests.conftest import assert_capture_str


class TestBaseSingleton:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        from src.singleton.singleton import Singleton

        assert_capture_str(capfd, ("インスタンスを生成しました\n", ""))
        assert Singleton.get_instance() == Singleton.get_instance()

    def test_exc_instantiation_error(self) -> None:
        # pylint: disable=unused-import
        from src.singleton.singleton import Singleton, _Singleton

        # pylint: enable=unused-import

        with pytest.raises(InstantiationError):
            _Singleton()


class TestTicketMaker:
    def test_normal(self) -> None:
        from src.singleton.ticket_maker import TicketMaker

        DEFAULT_TICKET_NUMBER = 1000
        assert TicketMaker.get_instance() == TicketMaker.get_instance()
        assert TicketMaker.get_next_ticket_number() == DEFAULT_TICKET_NUMBER + 0
        assert TicketMaker.get_next_ticket_number() == DEFAULT_TICKET_NUMBER + 1


class TestTripleton:
    def test_normal(self) -> None:
        from src.singleton.tripleton import Tripleton

        assert Tripleton.get_instance(0) == Tripleton.get_instance(0)
        assert Tripleton.get_instance(1) == Tripleton.get_instance(1)
        assert Tripleton.get_instance(2) == Tripleton.get_instance(2)
        # pylint: disable=protected-access
        assert Tripleton.get_instance(0)._id == 0
        assert Tripleton.get_instance(1)._id == 1
        assert Tripleton.get_instance(2)._id == 2
        # pylint: enable=protected-access

    def test_exc_instantiation_error(self) -> None:
        # pylint: disable=unused-import
        from src.singleton.tripleton import Tripleton, _Tripleton

        # pylint: enable=unused-import
        with pytest.raises(InstantiationError):
            _Tripleton(_id=3)
