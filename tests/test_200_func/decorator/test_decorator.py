from typing import Final

import pytest

from src.decorator.display import DisplayABC
from src.decorator.full_border import FullBorder
from src.decorator.multi_string_display import MultiStringDisplay
from src.decorator.side_border import SideBorder
from src.decorator.string_display import StringDisplay
from src.decorator.updown_border import UpdownBorder

STRING_DISPLAY: Final[StringDisplay] = StringDisplay(string="Hello, world.")
MULTI_STRING_DISPLAY: Final[MultiStringDisplay] = MultiStringDisplay()
MULTI_STRING_DISPLAY.add("Good morning.")
MULTI_STRING_DISPLAY.add("Hello.")
MULTI_STRING_DISPLAY.add("Good night, See you tomorrow.")


class TestStringDisplay:
    def test_normal(self) -> None:
        print("")
        STRING_DISPLAY.show()


class TestMultiStringDisplay:
    def test_normal(self) -> None:
        print("")
        MULTI_STRING_DISPLAY.show()


@pytest.mark.parametrize(("display"), [(STRING_DISPLAY), (MULTI_STRING_DISPLAY)])
class TestSideBorder:
    def test_normal(self, display: DisplayABC) -> None:
        print("")
        disp = SideBorder(display=display, char_border="#")
        disp.show()


@pytest.mark.parametrize(("display"), [(STRING_DISPLAY), (MULTI_STRING_DISPLAY)])
class TestFullBorder:
    def test_normal(self, display: DisplayABC) -> None:
        print("")
        disp = FullBorder(display=display)
        disp.show()


@pytest.mark.parametrize(("display"), [(STRING_DISPLAY), (MULTI_STRING_DISPLAY)])
class TestUpdownBorder:
    def test_normal(self, display: DisplayABC) -> None:
        print("")
        disp = UpdownBorder(display=display, char_border="-")
        disp.show()


@pytest.mark.parametrize(("display"), [(STRING_DISPLAY), (MULTI_STRING_DISPLAY)])
class TestComplex:
    def test_normal(self, display: DisplayABC) -> None:
        print("")
        disp = SideBorder(
            display=FullBorder(
                display=UpdownBorder(
                    display=SideBorder(
                        display=FullBorder(display=display),
                        char_border="*",
                    ),
                    char_border="@",
                ),
            ),
            char_border="/",
        )
        disp.show()
