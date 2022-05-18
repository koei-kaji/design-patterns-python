from random import Random
from typing import Final, List

from src.strategy.rock_paper_scissors.hand import Hand, HandEnum
from src.strategy.rock_paper_scissors.prob_strategy import ProbStrategy
from src.strategy.rock_paper_scissors.random_strategy import RandomStrategy
from src.strategy.rock_paper_scissors.winning_strategy import WinningStrategy

SEED: Final[int] = 314


class TestWinningStrategy:
    def test_same_seed(self) -> None:
        strategy_a = WinningStrategy(seed=SEED)
        strategy_b = WinningStrategy(seed=SEED)

        for _ in range(10):
            next_hand_a = strategy_a.next_hand()
            next_hand_b = strategy_b.next_hand()
            assert next_hand_a == next_hand_b

    def test_study(self) -> None:
        strategy = WinningStrategy(seed=SEED)

        strategy.study(True)
        strategy.study(True)
        assert strategy._won is True

        strategy.study(True)
        strategy.study(False)
        assert strategy._won is False

        strategy.study(False)  # type: ignore[unreachable]
        strategy.study(True)
        assert strategy._won is True

        strategy.study(False)
        strategy.study(False)
        assert strategy._won is False

    def test_next_hand_with_study_true(self) -> None:
        strategy = WinningStrategy(seed=SEED)
        first_hand = strategy.next_hand()

        strategy.study(True)
        for _ in range(10):
            assert strategy.next_hand() == first_hand

    def test_next_hand_with_study_false(self) -> None:
        strategy = WinningStrategy(seed=SEED)
        random_for_confirm = Random(SEED)

        _ = strategy.next_hand()
        strategy.study(False)
        for _ in range(10):
            assert strategy.next_hand() == Hand.get_hand(
                random_for_confirm.choice(list(HandEnum))
            )


class TestProbStrategy:
    def test_same_seed(self) -> None:
        strategy_a = ProbStrategy(seed=SEED)
        strategy_b = ProbStrategy(seed=SEED)

        for _ in range(10):
            next_hand_a = strategy_a.next_hand()
            next_hand_b = strategy_b.next_hand()
            assert next_hand_a == next_hand_b

    def test_get_sum(self) -> None:
        strategy = ProbStrategy(seed=SEED)

        expected_history: List[List[int]] = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        assert strategy._history == expected_history
        assert strategy._get_sum(HandEnum.ROCK) == sum(
            expected_history[HandEnum.ROCK.value]
        )
        assert strategy._get_sum(HandEnum.PAPER) == sum(
            expected_history[HandEnum.PAPER.value]
        )
        assert strategy._get_sum(HandEnum.SCISSORS) == sum(
            expected_history[HandEnum.SCISSORS.value]
        )

        expected_history = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        strategy._history = expected_history
        assert strategy._history == expected_history
        assert strategy._get_sum(HandEnum.ROCK) == sum(
            expected_history[HandEnum.ROCK.value]
        )
        assert strategy._get_sum(HandEnum.PAPER) == sum(
            expected_history[HandEnum.PAPER.value]
        )
        assert strategy._get_sum(HandEnum.SCISSORS) == sum(
            expected_history[HandEnum.SCISSORS.value]
        )

    def test_study_true(self) -> None:
        for prev_hand in HandEnum:
            for current_hand in HandEnum:
                strategy = ProbStrategy(seed=SEED)
                expected_history: List[List[int]] = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
                assert strategy._history == expected_history

                strategy._prev_hand = prev_hand
                strategy._current_hand = current_hand

                strategy.study(True)
                assert (
                    strategy._history[strategy._prev_hand.value][
                        strategy._current_hand.value
                    ]
                    == 1 + 1
                )
                assert (
                    strategy._history[strategy._prev_hand.value][
                        (strategy._current_hand.value + 1) % 3
                    ]
                    == 1
                )
                assert (
                    strategy._history[strategy._prev_hand.value][
                        (strategy._current_hand.value + 2) % 3
                    ]
                    == 1
                )
                assert (
                    strategy._history[(strategy._prev_hand.value + 1) % 3][
                        strategy._current_hand.value
                    ]
                    == 1
                )
                assert (
                    strategy._history[(strategy._prev_hand.value + 2) % 3][
                        strategy._current_hand.value
                    ]
                    == 1
                )

    def test_study_false(self) -> None:
        for prev_hand in HandEnum:
            for current_hand in HandEnum:
                strategy = ProbStrategy(seed=SEED)
                expected_history: List[List[int]] = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
                assert strategy._history == expected_history

                strategy._prev_hand = prev_hand
                strategy._current_hand = current_hand

                strategy.study(False)
                assert (
                    strategy._history[strategy._prev_hand.value][
                        strategy._current_hand.value
                    ]
                    == 1
                )
                assert (
                    strategy._history[strategy._prev_hand.value][
                        (strategy._current_hand.value + 1) % 3
                    ]
                    == 1 + 1
                )
                assert (
                    strategy._history[strategy._prev_hand.value][
                        (strategy._current_hand.value + 2) % 3
                    ]
                    == 1 + 1
                )
                assert (
                    strategy._history[(strategy._prev_hand.value + 1) % 3][
                        strategy._current_hand.value
                    ]
                    == 1
                )
                assert (
                    strategy._history[(strategy._prev_hand.value + 2) % 3][
                        strategy._current_hand.value
                    ]
                    == 1
                )

    def next_hand(self) -> None:
        # TODO: 面倒なので一旦パス
        pass


class TestRandomStrategy:
    def test_same_seed(self) -> None:
        strategy_a = RandomStrategy(seed=SEED)
        strategy_b = RandomStrategy(seed=SEED)

        for _ in range(10):
            next_hand_a = strategy_a.next_hand()
            next_hand_b = strategy_b.next_hand()
            assert next_hand_a == next_hand_b

    def test_study(self) -> None:
        pass

    def test_next_hand_with_study_true(self) -> None:
        strategy = WinningStrategy(seed=SEED)
        random_for_confirm = Random(SEED)

        for _ in range(10):
            hand = strategy.next_hand()
            assert hand == Hand.get_hand(random_for_confirm.choice(list(HandEnum)))
