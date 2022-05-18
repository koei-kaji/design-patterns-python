from random import Random
from typing import Any, List

from pydantic import BaseModel, PrivateAttr
from typing_extensions import Final

from ..common.custom_pydantic.config import BaseFrozenConfig


class Memento(BaseModel):
    money: int
    _fruits: List[str] = PrivateAttr(default=[])

    # narrow interface
    def get_money(self) -> int:
        return self.money

    # wide interface
    def _add_fruit(self, fruit: str) -> None:
        self._fruits.append(fruit)

    # wide interface
    def _copy_fruit(self) -> List[str]:
        return self._fruits.copy()

    class Config(BaseFrozenConfig):
        pass


FRUITS: Final[List[str]] = ["リンゴ", "ぶどう", "バナナ", "みかん"]


class Gamer(BaseModel):
    _money: int = PrivateAttr()
    _fruits: List[str] = PrivateAttr(default=[])
    _random: Random = PrivateAttr(default_factory=Random)

    def __init__(self, money: int, **data: Any) -> None:
        super().__init__(**data)
        self._money = money

    def get_money(self) -> int:
        return self._money

    def _acquire_fruit(self) -> str:
        prefix: str = ""
        if bool(self._random.getrandbits(1)):
            prefix = "おいしい"

        return f"{prefix}{self._random.choice(FRUITS)}"

    def bet(self) -> None:
        dice = self._random.randint(1, 6)
        if dice == 1:
            self._money += 100
            print("所持金が増えました")
        elif dice == 2:
            self._money = int(self._money / 2)
            print("所持金が半分になりました")
        elif dice == 6:
            fruit = self._acquire_fruit()
            print(f"フルーツ（{fruit}）をもらいました")
            self._fruits.append(fruit)
        else:
            print("何も起こりませんでした")

    def create_memento(self) -> Memento:
        memento = Memento(money=self._money)
        # フルーツはおいしいものだけ保存
        for fruit in self._fruits:
            if fruit.startswith("おいしい"):
                # pylint: disable=protected-access
                memento._add_fruit(fruit)
                # pylint: enable=protected-access

        return memento

    def restore_mement(self, memento: Memento) -> None:
        self._money = memento.money
        # pylint: disable=protected-access
        self._fruits = memento._copy_fruit()
        # pylint: enable=protected-access

    def __str__(self) -> str:
        return f"[money = {self._money}, fruits = {self._fruits}]"

    class Config(BaseFrozenConfig):
        pass
