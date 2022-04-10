from typing import Final

from src.strategy.rock_paper_scissors.player import Player
from src.strategy.rock_paper_scissors.prob_strategy import ProbStrategy
from src.strategy.rock_paper_scissors.random_strategy import RandomStrategy
from src.strategy.rock_paper_scissors.winning_strategy import WinningStrategy

SEED_A: Final[int] = 314
SEED_B: Final[int] = 15


class TestWinningStrategyVSWinningStrategy:
    def test_same_seed(self) -> None:
        player_a = Player(name="PlayerA", strategy=WinningStrategy(seed=SEED_A))
        player_b = Player(name="PlayerB", strategy=WinningStrategy(seed=SEED_A))

        for _ in range(10):
            hand_a = player_a.next_hand()
            hand_b = player_b.next_hand()

            assert hand_a == hand_b
            assert hand_a.is_stronger_than(hand_b) is False
            assert hand_b.is_stronger_than(hand_a) is False
            assert hand_a.is_weaker_than(hand_b) is False
            assert hand_b.is_weaker_than(hand_a) is False

            player_a.even()
            player_b.even()

            assert player_a._count_game == player_b._count_game
            assert player_a._count_win == player_b._count_win == 0
            assert player_a._count_lose == player_b._count_lose == 0

    def test_normal(self) -> None:
        player_a = Player(name="PlayerA", strategy=WinningStrategy(seed=SEED_A))
        player_b = Player(name="PlayerB", strategy=WinningStrategy(seed=SEED_B))

        for _ in range(10):
            hand_a = player_a.next_hand()
            hand_b = player_b.next_hand()

            if hand_a.is_stronger_than(hand_b):
                print(f"Winner:{player_a}")
                player_a.win()
                player_b.lose()
            elif hand_a.is_weaker_than(hand_b):
                print(f"Winner:{player_b}")
                player_a.lose()
                player_b.win()
            else:
                print("Even...")
                player_a.even()
                player_b.even()


class TestProbStrategyVSProbStrategy:
    def test_same_seed(self) -> None:
        player_a = Player(name="PlayerA", strategy=ProbStrategy(seed=SEED_A))
        player_b = Player(name="PlayerB", strategy=ProbStrategy(seed=SEED_A))

        for _ in range(10):
            hand_a = player_a.next_hand()
            hand_b = player_b.next_hand()

            assert hand_a == hand_b
            assert hand_a.is_stronger_than(hand_b) is False
            assert hand_b.is_stronger_than(hand_a) is False
            assert hand_a.is_weaker_than(hand_b) is False
            assert hand_b.is_weaker_than(hand_a) is False

            player_a.even()
            player_b.even()

            assert player_a._count_game == player_b._count_game
            assert player_a._count_win == player_b._count_win == 0
            assert player_a._count_lose == player_b._count_lose == 0

    def test_normal(self) -> None:
        player_a = Player(name="PlayerA", strategy=ProbStrategy(seed=SEED_A))
        player_b = Player(name="PlayerB", strategy=ProbStrategy(seed=SEED_B))

        for _ in range(10):
            hand_a = player_a.next_hand()
            hand_b = player_b.next_hand()

            if hand_a.is_stronger_than(hand_b):
                print(f"Winner:{player_a}")
                player_a.win()
                player_b.lose()
            elif hand_a.is_weaker_than(hand_b):
                print(f"Winner:{player_b}")
                player_a.lose()
                player_b.win()
            else:
                print("Even...")
                player_a.even()
                player_b.even()


class TestWinningStrategyVSProbStrategy:
    def test_normal(self) -> None:
        player_a = Player(name="PlayerA", strategy=WinningStrategy(seed=SEED_A))
        player_b = Player(name="PlayerB", strategy=ProbStrategy(seed=SEED_B))

        for _ in range(10):
            hand_a = player_a.next_hand()
            hand_b = player_b.next_hand()

            if hand_a.is_stronger_than(hand_b):
                print(f"Winner:{player_a}")
                player_a.win()
                player_b.lose()
            elif hand_a.is_weaker_than(hand_b):
                print(f"Winner:{player_b}")
                player_a.lose()
                player_b.win()
            else:
                print("Even...")
                player_a.even()
                player_b.even()


class TestRandomStrategyVSRandomStrategy:
    def test_same_seed(self) -> None:
        player_a = Player(name="PlayerA", strategy=RandomStrategy(seed=SEED_A))
        player_b = Player(name="PlayerB", strategy=RandomStrategy(seed=SEED_A))

        for _ in range(10):
            hand_a = player_a.next_hand()
            hand_b = player_b.next_hand()

            assert hand_a == hand_b
            assert hand_a.is_stronger_than(hand_b) is False
            assert hand_b.is_stronger_than(hand_a) is False
            assert hand_a.is_weaker_than(hand_b) is False
            assert hand_b.is_weaker_than(hand_a) is False

            player_a.even()
            player_b.even()

            assert player_a._count_game == player_b._count_game
            assert player_a._count_win == player_b._count_win == 0
            assert player_a._count_lose == player_b._count_lose == 0

    def test_normal(self) -> None:
        player_a = Player(name="PlayerA", strategy=RandomStrategy(seed=SEED_A))
        player_b = Player(name="PlayerB", strategy=RandomStrategy(seed=SEED_B))

        for _ in range(10):
            hand_a = player_a.next_hand()
            hand_b = player_b.next_hand()

            if hand_a.is_stronger_than(hand_b):
                print(f"Winner:{player_a}")
                player_a.win()
                player_b.lose()
            elif hand_a.is_weaker_than(hand_b):
                print(f"Winner:{player_b}")
                player_a.lose()
                player_b.win()
            else:
                print("Even...")
                player_a.even()
                player_b.even()
