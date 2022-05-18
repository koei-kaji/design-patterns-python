import pytest

from src.facade.page_maker.page_maker import PageMaker


@pytest.mark.usefixtures("chdir_to_tmpdir")
class TestPageMaker:
    # pylint: disable=unused-argument
    def test_normal_make_welcome_page(self) -> None:
        # NOTE: テストは面倒なのでとりあえず標準出力
        print("")
        PageMaker.make_welcome_page("ned@stark.com", "welcome.html")

        with open("welcome.html", mode="r", encoding="utf-8") as f:
            print("")
            print("".join(f.readlines()))

    def test_normal_make_link_page(self) -> None:
        # NOTE: テストは面倒なのでとりあえず標準出力
        print("")
        PageMaker.make_link_page("linkpage.html")

        with open("linkpage.html", mode="r", encoding="utf-8") as f:
            print("")
            print("".join(f.readlines()))
