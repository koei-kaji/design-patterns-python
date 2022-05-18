from typing import Final, List, cast

from pytest import CaptureFixture

from src.factory_method.idcard.idcard import IDCard, IDCardWithSerial
from src.factory_method.idcard.idcard_factory import (
    IDCardFactory,
    IDCardWithSerialFactory,
)
from tests.conftest import assert_capture_str


def assert_idcard_create(capfd: CaptureFixture[str], card: IDCard) -> None:
    assert_capture_str(capfd, (f"{card.get_owner()}のカードを作ります\n", ""))


def assert_idcard_use(capfd: CaptureFixture[str], card: IDCard) -> None:
    assert_capture_str(capfd, (f"{card.get_owner()}のカードを使います\n", ""))


def assert_idcard_with_serial_create(
    capfd: CaptureFixture[str], card: IDCardWithSerial
) -> None:
    assert_capture_str(
        capfd, (f"{card.get_owner()}({card.get_serial()})のカードを作ります\n", "")
    )


def assert_idcard_with_serial_use(
    capfd: CaptureFixture[str], card: IDCardWithSerial
) -> None:
    assert_capture_str(
        capfd, (f"{card.get_owner()}({card.get_serial()})のカードを使います\n", "")
    )


class TestIDCard:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        OWNERS: Final[List[str]] = ["オーナー", "owner"]
        factory = IDCardFactory()

        card1 = factory.create(OWNERS[0])
        assert_idcard_create(capfd, cast(IDCard, card1))
        card2 = factory.create(OWNERS[1])
        assert_idcard_create(capfd, cast(IDCard, card2))

        card1.use()
        assert_idcard_use(capfd, cast(IDCard, card1))
        card2.use()
        assert_idcard_use(capfd, cast(IDCard, card2))

        assert cast(IDCard, card1).get_owner() == OWNERS[0]
        assert cast(IDCard, card2).get_owner() == OWNERS[1]

    def test_normal_stdout(self) -> None:
        OWNERS: Final[List[str]] = ["オーナー", "owner"]

        factory = IDCardFactory()
        print("")
        card1 = factory.create(OWNERS[0])
        card2 = factory.create(OWNERS[1])
        card1.use()
        card2.use()


class TestIDCardWithSerial:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        # pylint: disable=protected-access
        SERIAL_DEFAULT: Final[int] = IDCardWithSerialFactory()._serial
        # pylint: enable=protected-access

        OWNERS: Final[List[str]] = ["オーナー", "owner"]
        factory = IDCardWithSerialFactory()

        card1 = factory.create(OWNERS[0])
        assert_idcard_with_serial_create(capfd, cast(IDCardWithSerial, card1))
        card2 = factory.create(OWNERS[1])
        assert_idcard_with_serial_create(capfd, cast(IDCardWithSerial, card2))

        card1.use()
        assert_idcard_with_serial_use(capfd, cast(IDCardWithSerial, card1))
        card2.use()
        assert_idcard_with_serial_use(capfd, cast(IDCardWithSerial, card2))

        assert cast(IDCardWithSerial, card1).get_owner() == OWNERS[0]
        assert cast(IDCardWithSerial, card2).get_owner() == OWNERS[1]
        assert cast(IDCardWithSerial, card1).get_serial() == SERIAL_DEFAULT + 0
        assert cast(IDCardWithSerial, card2).get_serial() == SERIAL_DEFAULT + 1

    def test_normal_stdout(self) -> None:
        OWNERS: Final[List[str]] = ["オーナー", "owner"]
        factory = IDCardWithSerialFactory()

        print("")
        card1 = factory.create(OWNERS[0])
        card2 = factory.create(OWNERS[1])
        card1.use()
        card2.use()
