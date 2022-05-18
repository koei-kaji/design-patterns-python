import tracemalloc
from typing import List

from src.flyweight.big_string import BigString


class TestBigString:
    def test_normal_shared(self) -> None:
        big_string = BigString(string="1-1-2")

        # TODO: テストが面倒なので標準出力してるだけ
        print()
        big_string.print()

    def test_normal_unshared(self) -> None:
        big_string = BigString(string="1-1-2")

        # TODO: テストが面倒なので標準出力してるだけ
        print()
        big_string.print()

    def test_check_memory_usage(self) -> None:
        def allocate(is_shared: bool) -> None:
            tracemalloc.start()
            big_strings: List[BigString] = []
            for _ in range(1000):
                big_strings.append(BigString(string="1212123", is_shared=is_shared))
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics("filename")
            tracemalloc.stop()

            for stat in top_stats[:3]:
                print(stat)

        print()
        print("共有した場合：")
        allocate(True)
        print("共有しない場合：")
        allocate(False)
