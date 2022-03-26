from multiprocessing import dummy
from typing import Tuple

from pytest import CaptureFixture

from src.adapter.delegation_pattern.print import PrintABC as DelegatePrint
from src.adapter.delegation_pattern.print_banner import (
    PrintBanner as DelegatePrintBanner,
)
from src.adapter.inheritance_pattern.print import PrintABC as InheritPrint
from src.adapter.inheritance_pattern.print_banner import (
    PrintBanner as InheritPrintBanner,
)


def assert_capture(capfd: CaptureFixture, expected: Tuple[str, str]):
    result = capfd.readouterr()
    assert result.out == expected[0]
    assert result.err == expected[1]


def format_weak(string: str):
    return f"({string})"


def format_strong(string: str):
    return f"*{string}*"


class TestInheritancePattern:
    def test_normal(self, capfd: CaptureFixture):
        DUMMY_STR = "Dummy"
        print_banner: InheritPrint = InheritPrintBanner(DUMMY_STR)

        print_banner.print_weak()
        assert_capture(capfd, (f"{format_weak(DUMMY_STR)}\n", ""))

        print_banner.print_strong()
        assert_capture(capfd, (f"{format_strong(DUMMY_STR)}\n", ""))


class TestDelegationPattern:
    def test_normal(self, capfd: CaptureFixture):
        DUMMY_STR = "Dummy"
        print_banner: DelegatePrint = DelegatePrintBanner(DUMMY_STR)

        print_banner.print_weak()
        assert_capture(capfd, (f"{format_weak(DUMMY_STR)}\n", ""))

        print_banner.print_strong()
        assert_capture(capfd, (f"{format_strong(DUMMY_STR)}\n", ""))
