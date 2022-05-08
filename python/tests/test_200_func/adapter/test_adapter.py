from pytest import CaptureFixture

from src.adapter.delegation_pattern.print import PrintABC as DelegatePrint
from src.adapter.delegation_pattern.print_banner import (
    PrintBanner as DelegatePrintBanner,
)
from src.adapter.inheritance_pattern.print import PrintIF as InheritPrint
from src.adapter.inheritance_pattern.print_banner import (
    PrintBanner as InheritPrintBanner,
)
from tests.conftest import assert_capture_str


def format_weak(string: str) -> str:
    return f"({string})"


def format_strong(string: str) -> str:
    return f"*{string}*"


class TestInheritancePattern:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        DUMMY_STR = "Dummy"
        print_banner: InheritPrint = InheritPrintBanner(string=DUMMY_STR)

        print_banner.print_weak()
        assert_capture_str(capfd, (f"{format_weak(DUMMY_STR)}\n", ""))

        print_banner.print_strong()
        assert_capture_str(capfd, (f"{format_strong(DUMMY_STR)}\n", ""))


class TestDelegationPattern:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        DUMMY_STR = "Dummy"
        print_banner: DelegatePrint = DelegatePrintBanner(string=DUMMY_STR)

        print_banner.print_weak()
        assert_capture_str(capfd, (f"{format_weak(DUMMY_STR)}\n", ""))

        print_banner.print_strong()
        assert_capture_str(capfd, (f"{format_strong(DUMMY_STR)}\n", ""))
