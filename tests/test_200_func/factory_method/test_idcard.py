from typing import cast

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
        owners = ["オーナー", "owner"]
        factory = IDCardFactory()

        card1 = factory.create(owners[0])
        assert_idcard_create(capfd, cast(IDCard, card1))
        card2 = factory.create(owners[1])
        assert_idcard_create(capfd, cast(IDCard, card2))

        card1.use()
        assert_idcard_use(capfd, cast(IDCard, card1))
        card2.use()
        assert_idcard_use(capfd, cast(IDCard, card2))

        assert cast(IDCard, card1).get_owner() == owners[0]
        assert cast(IDCard, card2).get_owner() == owners[1]


class TestIDCardWithSerial:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        # pylint: disable=protected-access
        serial_default = IDCardWithSerialFactory()._serial
        # pylint: enable=protected-access

        owners = ["オーナー", "owner"]
        factory = IDCardWithSerialFactory()

        card1 = factory.create(owners[0])
        assert_idcard_with_serial_create(capfd, cast(IDCardWithSerial, card1))
        card2 = factory.create(owners[1])
        assert_idcard_with_serial_create(capfd, cast(IDCardWithSerial, card2))

        card1.use()
        assert_idcard_with_serial_use(capfd, cast(IDCardWithSerial, card1))
        card2.use()
        assert_idcard_with_serial_use(capfd, cast(IDCardWithSerial, card2))

        assert cast(IDCardWithSerial, card1).get_owner() == owners[0]
        assert cast(IDCardWithSerial, card2).get_owner() == owners[1]
        assert cast(IDCardWithSerial, card1).get_serial() == serial_default + 0
        assert cast(IDCardWithSerial, card2).get_serial() == serial_default + 1
