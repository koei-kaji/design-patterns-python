import pickle
from time import sleep
from typing import Optional

import pytest
from typing_extensions import Final

from src.memento.game import Gamer, Memento


class TestGame:
    def test_normal(self) -> None:
        gamer = Gamer(money=100)
        memento = gamer.create_memento()  # 最初の状態を残しておく

        for i in range(10):
            print(f"==={i}")
            print(f"現状:{gamer}")

            gamer.bet()

            print(f"所持金は{gamer.get_money()}円になりました")

            if gamer.get_money() > memento.get_money():
                print("    （だいぶ増えたので、現在の状態を保存しておこう）")
                memento = gamer.create_memento()
            elif gamer.get_money() < (memento.get_money() / 2):
                print("    （だいぶ減ったので、以前の状態に復帰しよう）")
                gamer.restore_mement(memento)

            sleep(0.1)


@pytest.mark.usefixtures("chdir_to_tmpdir")
class TestGameWithPickle:
    SAVE_FILE_NAME: Final[str] = "game.pkl"

    def load_memento(self) -> Optional[Memento]:
        memento: Optional[Memento] = None

        try:
            with open(self.SAVE_FILE_NAME, "rb") as f:
                memento = pickle.load(f)
        except FileNotFoundError as error:
            print(error)

        return memento

    def save_memento(self, memento: Memento) -> None:
        with open(self.SAVE_FILE_NAME, "wb") as f:
            pickle.dump(memento, f)

    def main(self) -> None:
        gamer = Gamer(money=100)
        memento = self.load_memento()
        if memento is not None:
            print("前回保存した結果からスタートします")
            gamer.restore_mement(memento)
        else:
            print("新規にスタートします")
            memento = gamer.create_memento()

        for i in range(10):
            print(f"==={i}")
            print(f"現状:{gamer}")

            gamer.bet()

            print(f"所持金は{gamer.get_money()}円になりました")

            if gamer.get_money() > memento.get_money():
                print("    （だいぶ増えたので、現在の状態を保存しておこう）")
                memento = gamer.create_memento()
                self.save_memento(memento)

            elif gamer.get_money() < (memento.get_money() / 2):
                print("    （だいぶ減ったので、以前の状態に復帰しよう）")
                gamer.restore_mement(memento)

            sleep(0.1)

    def test_normal(self) -> None:
        # 1回目
        self.main()

        # 2回目
        self.main()
