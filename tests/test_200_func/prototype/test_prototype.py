from typing import Final, Tuple

from pytest import CaptureFixture

from src.prototype.framework.manager import Manager
from src.prototype.framework.product import ProductABC
from src.prototype.message_box import MessageBox
from src.prototype.underline_pen import UnderlinePen
from tests.conftest import assert_capture_str


class TestMessageBox:
    def assert_capture(
        self,
        capfd: CaptureFixture[str],
        product: ProductABC,
        decochar: str,
        message: str,
    ) -> None:
        product.use(message)
        assert_capture_str(
            capfd,
            (
                "\n".join(
                    [
                        "",
                        f"{decochar * (len(message) + 4)}",
                        f"{decochar} {message} {decochar}",
                        f"{decochar * (len(message) + 4)}",
                        "",
                    ]
                ),
                "",
            ),
        )

    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        STRONG: Final[Tuple[str, str, str]] = ("*", "strong", "Hello, strong.")
        SLASH: Final[Tuple[str, str, str]] = ("/", "slash", "Hello, slash.")

        manager = Manager()
        manager.register(STRONG[1], MessageBox(decochar=STRONG[0]))
        manager.register(SLASH[1], MessageBox(decochar=SLASH[0]))

        # showcaseに登録されているかどうか
        # pylint: disable=protected-access
        assert (STRONG[1] in manager._showcase) is True
        assert (SLASH[1] in manager._showcase) is True
        # pylint: enable=protected-access

        # 出力内容の確認
        product_strong = manager.create(STRONG[1])
        self.assert_capture(capfd, product_strong, STRONG[0], STRONG[2])
        product_slash = manager.create(SLASH[1])
        self.assert_capture(capfd, product_slash, SLASH[0], SLASH[2])

        # createされるインスタンスは異なるものかどうか
        product_strong_2nd = manager.create(STRONG[1])
        product_slash_2nd = manager.create(SLASH[1])
        assert id(product_strong_2nd) != id(product_strong)
        assert id(product_slash_2nd) != id(product_slash)

    def test_normal_stdout(self) -> None:
        STRONG: Final[Tuple[str, str, str]] = ("*", "strong", "Hello, strong.")
        SLASH: Final[Tuple[str, str, str]] = ("/", "slash", "Hello, slash.")

        manager = Manager()
        manager.register(STRONG[1], MessageBox(decochar=STRONG[0]))
        manager.register(SLASH[1], MessageBox(decochar=SLASH[0]))

        manager.create(STRONG[1]).use(STRONG[2])
        manager.create(SLASH[1]).use(SLASH[2])


class TestUnderlinePen:
    def assert_capture(
        self, capfd: CaptureFixture[str], product: ProductABC, ulchar: str, message: str
    ) -> None:
        product.use(message)
        assert_capture_str(
            capfd,
            (
                "\n".join(
                    [
                        "",
                        f'"{message}"',
                        f" {ulchar * len(message)} ",
                        "",
                    ]
                ),
                "",
            ),
        )

    def test_normal(self, capfd: CaptureFixture[str]) -> None:
        STRONG: Final[Tuple[str, str, str]] = ("=", "strong", "Hello, strong.")
        WEAK: Final[Tuple[str, str, str]] = ("-", "weak", "Hello, weak.")

        manager = Manager()
        manager.register(STRONG[1], UnderlinePen(ulchar=STRONG[0]))
        manager.register(WEAK[1], UnderlinePen(ulchar=WEAK[0]))

        # showcaseに登録されているかどうか
        # pylint: disable=protected-access
        assert (STRONG[1] in manager._showcase) is True
        assert (WEAK[1] in manager._showcase) is True
        # pylint: enable=protected-access

        # 出力内容の確認
        product_strong = manager.create(STRONG[1])
        self.assert_capture(capfd, product_strong, STRONG[0], STRONG[2])
        product_weak = manager.create(WEAK[1])
        self.assert_capture(capfd, product_weak, WEAK[0], WEAK[2])

        # createされるインスタンスは異なるものかどうか
        product_strong_2nd = manager.create(STRONG[1])
        product_slash_2nd = manager.create(WEAK[1])
        assert id(product_strong_2nd) != id(product_strong)
        assert id(product_slash_2nd) != id(product_weak)

    def test_normal_stdout(self) -> None:
        STRONG: Final[Tuple[str, str, str]] = ("=", "strong", "Hello, strong.")
        WEAK: Final[Tuple[str, str, str]] = ("-", "weak", "Hello, weak.")

        manager = Manager()
        manager.register(STRONG[1], UnderlinePen(ulchar=STRONG[0]))
        manager.register(WEAK[1], UnderlinePen(ulchar=WEAK[0]))

        # 出力内容の確認
        manager.create(STRONG[1]).use(STRONG[2])
        manager.create(WEAK[1]).use(WEAK[2])
