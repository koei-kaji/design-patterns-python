import os
import threading

import pytest

from src.observer.digit_observer import DigitObserver
from src.observer.graph_observer import GraphObserver
from src.observer.incremental_number_generator import IncrementalNumberGenerator
from src.observer.number_generator import NumberGeneratorABC
from src.observer.random_number_generator import RandomNumberGenerator
from src.observer.tk_observer import TkObserver


def set_observer(generator: NumberGeneratorABC) -> None:
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)


class TestRandomNumberGenerator:
    def test_normal(self) -> None:
        generator = RandomNumberGenerator()
        set_observer(generator)

        # TODO: テストが面倒なのでとりあえず標準出力
        print("")
        generator.publish()


class TestIncrementalNumberGenerator:
    def test_normal(self) -> None:
        generator = IncrementalNumberGenerator(start=10, end=50, increment=5)
        set_observer(generator)

        # TODO: テストが面倒なのでとりあえず標準出力
        print("")
        generator.publish()


@pytest.mark.skipif(
    condition=(os.environ.get("GITHUB_ACTIONS") == "true"),
    reason="Needs to be interactive.",
)
class TestTkObserver:
    def test_normal(self) -> None:
        generator = RandomNumberGenerator()
        observer = TkObserver()
        generator.add_observer(observer)

        # NOTE: tkinterはメインスレッドにするのが妥当らしい
        thread = threading.Thread(target=generator.publish)
        thread.start()

        observer.after(5000, observer.destroy)
        observer.mainloop()
