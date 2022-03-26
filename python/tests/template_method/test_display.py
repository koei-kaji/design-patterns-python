from pytest import CaptureFixture

from src.template_method.custom_type import Char
from src.template_method.display import CharDisplay, StringDisplay
from tests.conftest import assert_capture_str


class TestCharDisplay:
    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        display = CharDisplay(char=Char("H"))
        display.display()
        assert_capture_str(capfd, ("<<HHHHH>>\n", ""))


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
