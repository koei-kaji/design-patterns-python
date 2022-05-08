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

    @pytest.mark.parametrize(("char"), [("", "two")])
    def test_exc_not_char(self, char: str) -> None:
        with pytest.raises(ValidationError):
            CharDisplay(char=char)


class TestStringDisplay:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        string = "Hello, World!"
        display = StringDisplay(string=string)
        display.display()
        assert_capture_str(
            capfd,
            (
                "\n".join(
                    [
                        "",
                        f"+{'-' * len(string)}+",
                        *[f"|{string}|" for _ in range(5)],
                        f"+{'-' * len(string)}+",
                        "",
                    ]
                ),
                "",
            ),
        )
