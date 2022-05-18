from typing import Final

import pytest
from pydantic import ValidationError
from pytest import CaptureFixture

from src.template_method.display import CharDisplay, StringDisplay
from tests.conftest import assert_capture_str


class TestCharDisplay:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        display = CharDisplay(char="H")
        display.display()
        assert_capture_str(capfd, ("<<HHHHH>>\n", ""))

    def test_normal_stdout(self) -> None:
        display = CharDisplay(char="H")
        print("")
        display.display()

    @pytest.mark.parametrize(("char"), [("", "two")])
    def test_exc_not_char(self, char: str) -> None:
        with pytest.raises(ValidationError):
            CharDisplay(char=char)


class TestStringDisplay:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        STRING: Final[str] = "Hello, World!"
        display = StringDisplay(string=STRING)
        display.display()
        assert_capture_str(
            capfd,
            (
                "\n".join(
                    [
                        "",
                        f"+{'-' * len(STRING)}+",
                        *[f"|{STRING}|" for _ in range(5)],
                        f"+{'-' * len(STRING)}+",
                        "",
                    ]
                ),
                "",
            ),
        )

    def test_normal_stdout(self) -> None:
        string = "Hello, World!"
        display = StringDisplay(string=string)
        print("")
        display.display()
