import os

import pytest

from src.builder.director import Director
from src.builder.html_builder import DEFAULT_ENCODING, HTMLBuilder
from src.builder.text_builder import TextBuilder
from src.builder.tk_builder import TkBuilder
from tests.conftest import ChdirToTmpdirFixture


class TestTextBuilder:
    def test_normal(self) -> None:
        text_builder = TextBuilder()
        director = Director(builder=text_builder)
        director.construct_()
        result = text_builder.get_result()

        # NOTE: テストは面倒なのでとりあえず標準出力
        print(result)


class TestHTMLBuilder:
    # pylint: disable=unused-argument
    def test_normal(self, chdir_to_tmpdir: ChdirToTmpdirFixture) -> None:
        html_builder = HTMLBuilder()
        director = Director(builder=html_builder)
        director.construct_()

        result = html_builder.get_result()

        # NOTE: テストは面倒なのでとりあえず標準出力
        with open(result, mode="r", encoding=DEFAULT_ENCODING) as f:
            print("")
            print("".join(f.readlines()))


class TestTkBuilder:
    @pytest.mark.skipif(
        condition=(os.environ.get("GITHUB_ACTIONS") == "true"),
        reason="Needs to be interactive.",
    )
    def test_normal(self) -> None:
        tk_builder = TkBuilder()
        director = Director(builder=tk_builder)
        director.construct_()

        result = tk_builder.get_result()

        # NOTE: テストは面倒なのでとりあえず標準出力
        # pylint: disable=unnecessary-lambda
        result.after(3000, lambda: result.destroy())
        # pylint: enable=unnecessary-lambda
        result.mainloop()
