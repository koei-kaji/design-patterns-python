from typing import Final

from src.bridge.char_display_impl import CharDisplayImpl
from src.bridge.count_display import CountDisplay
from src.bridge.display import Display
from src.bridge.file_display_impl import DEFAULT_ENCODING, FileDisplayImpl
from src.bridge.increase_display import IncreaseDisplay
from src.bridge.random_count_display import RandomCountDisplay
from src.bridge.string_display_impl import StringDisplayImpl
from src.common.custom_pydantic.types import Char
from tests.conftest import ChdirToTmpdirFixture


class TestDisplayWithStringDisplayImpl:
    def test_normal(self) -> None:
        DUMMY_STRING: Final[str] = "Hello, World"
        display = Display(impl=StringDisplayImpl(string=DUMMY_STRING))

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display()


class TestCountDisplayWithStringDisplayImpl:
    def test_normal(self) -> None:
        DUMMY_STRING: Final[str] = "Hello, World"
        display = CountDisplay(impl=StringDisplayImpl(string=DUMMY_STRING))

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display()

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display_multi(2)


class TestRandomCountDisplayWithStringDisplayImpl:
    def test_normal(self) -> None:
        DUMMY_STRING: Final[str] = "Hello, World"
        display = RandomCountDisplay(impl=StringDisplayImpl(string=DUMMY_STRING))

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display()

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display_multi(2)

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display_multi_random(5)


class TestCountDisplayWithFileDisplayImpl:
    # pylint: disable=unused-argument
    def test_normal(self, chdir_to_tmpdir: ChdirToTmpdirFixture) -> None:
        DUMMY_FILENAME: Final[str] = "dummy.txt"
        with open(DUMMY_FILENAME, mode="w", encoding=DEFAULT_ENCODING) as f:
            f.write(
                "\n".join(
                    [
                        "Twinkle, twinkle, little star,",
                        "How I wonder what you are.",
                        "Twinkle, twinkle, little star,",
                        "How I wonder what you are.",
                        "Twinkle, twinkle, little star,",
                        "How I wonder what you are.",
                    ]
                )
            )

        display = CountDisplay(impl=FileDisplayImpl(filename=DUMMY_FILENAME))

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display()

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display.display_multi(2)

    # pylint: enable=unused-argument


class TestIncreaseDisplayWithCharDisplayImpl:
    def test_normal(self) -> None:
        display1 = IncreaseDisplay(
            impl=CharDisplayImpl(
                head=Char("<"),
                body=Char("*"),
                foot=Char(">"),
            ),
            step=1,
        )
        display2 = IncreaseDisplay(
            impl=CharDisplayImpl(
                head=Char("|"),
                body=Char("#"),
                foot=Char("-"),
            ),
            step=2,
        )

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display1.display_increasily(4)

        # NOTE: テストが面倒なのでとりあえず標準出力
        print("")
        display2.display_increasily(6)
