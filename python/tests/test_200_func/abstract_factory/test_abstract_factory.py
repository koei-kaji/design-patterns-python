import pytest
from py._path.local import LocalPath
from pytest import MonkeyPatch

from src.abstract_factory.factory.factory import FactoryABC
from src.abstract_factory.factory.page import DEFAULT_ENCODING


@pytest.mark.parametrize(
    "class_name",
    [
        "src.abstract_factory.list_factory.list_factory.ListFactory",
        "src.abstract_factory.table_factory.table_factory.TableFactory",
    ],
)
class TestFactory:
    def test_normal(
        self, tmpdir: LocalPath, monkeypatch: MonkeyPatch, class_name: str
    ) -> None:
        monkeypatch.chdir(tmpdir)

        factory = FactoryABC.get_factory(class_name)

        link_asahi = factory.create_link("朝日新聞", "http://www.asahi.com/")
        link_yomiuri = factory.create_link("読売新聞", "http://yomiuri.co.jp/")
        link_yahoo_us = factory.create_link("Yahoo!", "http://www.yahoo.com/")
        link_yahoo_jp = factory.create_link("Yahoo!Japan", "http://www.yahoo.co.jp/")
        link_excite = factory.create_link("Excite", "http://www.excite.com/")
        link_google = factory.create_link("Google", "http://www.google.com/")

        tray_news = factory.create_tray("新聞")
        tray_news.add(link_asahi)
        tray_news.add(link_yomiuri)

        tray_yahoo = factory.create_tray("Yahoo!")
        tray_yahoo.add(link_yahoo_us)
        tray_yahoo.add(link_yahoo_jp)

        tray_search = factory.create_tray("サーチエンジン")
        tray_search.add(tray_yahoo)
        tray_search.add(link_excite)
        tray_search.add(link_google)

        page = factory.create_page("LinkPage", "AUTHOR")
        page.add(tray_news)
        page.add(tray_search)
        result = page.output()

        # NOTE: テストは面倒なのでとりあえず標準出力
        with open(result, mode="r", encoding=DEFAULT_ENCODING) as f:
            print("")
            print("".join(f.readlines()))

    def test_yahoo(
        self, tmpdir: LocalPath, monkeypatch: MonkeyPatch, class_name: str
    ) -> None:
        monkeypatch.chdir(tmpdir)

        factory = FactoryABC.get_factory(class_name)
        page = factory.create_yahoo_page()
        result = page.output()

        # NOTE: テストは面倒なのでとりあえず標準出力
        with open(result, mode="r", encoding=DEFAULT_ENCODING) as f:
            print("")
            print("".join(f.readlines()))
