from src.strategy.rock_paper_scissors.hand import Hand, HandEnum, ResultEnum


def assert_fight_result(own: HandEnum, other: HandEnum, expect: ResultEnum) -> None:
    # pylint: disable=protected-access
    assert Hand.get_hand(own)._fight(Hand.get_hand(other)) == expect


def assert_is_stronger_than_result(
    own: HandEnum, other: HandEnum, expect: bool
) -> None:
    assert Hand.get_hand(own).is_stronger_than(Hand.get_hand(other)) is expect


def assert_is_weaker_than_result(own: HandEnum, other: HandEnum, expect: bool) -> None:
    assert Hand.get_hand(own).is_weaker_than(Hand.get_hand(other)) is expect


class TestHand:
    def test_instantiation(self) -> None:
        assert id(Hand.get_hand(HandEnum.ROCK)) == id(Hand.get_hand(HandEnum.ROCK))
        assert id(Hand.get_hand(HandEnum.SCISSORS)) == id(
            Hand.get_hand(HandEnum.SCISSORS)
        )
        assert id(Hand.get_hand(HandEnum.PAPER)) == id(Hand.get_hand(HandEnum.PAPER))

        # pylint: disable=protected-access
        assert Hand.get_hand(HandEnum.ROCK)._hand == HandEnum.ROCK
        assert Hand.get_hand(HandEnum.SCISSORS)._hand == HandEnum.SCISSORS
        assert Hand.get_hand(HandEnum.PAPER)._hand == HandEnum.PAPER

    def test_fight(self) -> None:
        assert_fight_result(HandEnum.ROCK, HandEnum.ROCK, ResultEnum.DRAW)
        assert_fight_result(HandEnum.ROCK, HandEnum.PAPER, ResultEnum.DEFEAT)
        assert_fight_result(HandEnum.ROCK, HandEnum.SCISSORS, ResultEnum.VICTORY)
        assert_fight_result(HandEnum.PAPER, HandEnum.ROCK, ResultEnum.VICTORY)
        assert_fight_result(HandEnum.PAPER, HandEnum.PAPER, ResultEnum.DRAW)
        assert_fight_result(HandEnum.PAPER, HandEnum.SCISSORS, ResultEnum.DEFEAT)
        assert_fight_result(HandEnum.SCISSORS, HandEnum.ROCK, ResultEnum.DEFEAT)
        assert_fight_result(HandEnum.SCISSORS, HandEnum.PAPER, ResultEnum.VICTORY)
        assert_fight_result(HandEnum.SCISSORS, HandEnum.SCISSORS, ResultEnum.DRAW)

    def test_is_stronger_than(self) -> None:
        assert_is_stronger_than_result(HandEnum.ROCK, HandEnum.ROCK, False)
        assert_is_stronger_than_result(HandEnum.ROCK, HandEnum.PAPER, False)
        assert_is_stronger_than_result(HandEnum.ROCK, HandEnum.SCISSORS, True)
        assert_is_stronger_than_result(HandEnum.PAPER, HandEnum.ROCK, True)
        assert_is_stronger_than_result(HandEnum.PAPER, HandEnum.PAPER, False)
        assert_is_stronger_than_result(HandEnum.PAPER, HandEnum.SCISSORS, False)
        assert_is_stronger_than_result(HandEnum.SCISSORS, HandEnum.ROCK, False)
        assert_is_stronger_than_result(HandEnum.SCISSORS, HandEnum.PAPER, True)
        assert_is_stronger_than_result(HandEnum.SCISSORS, HandEnum.SCISSORS, False)

    def test_is_weaker_than(self) -> None:
        assert_is_weaker_than_result(HandEnum.ROCK, HandEnum.ROCK, False)
        assert_is_weaker_than_result(HandEnum.ROCK, HandEnum.PAPER, True)
        assert_is_weaker_than_result(HandEnum.ROCK, HandEnum.SCISSORS, False)
        assert_is_weaker_than_result(HandEnum.PAPER, HandEnum.ROCK, False)
        assert_is_weaker_than_result(HandEnum.PAPER, HandEnum.PAPER, False)
        assert_is_weaker_than_result(HandEnum.PAPER, HandEnum.SCISSORS, True)
        assert_is_weaker_than_result(HandEnum.SCISSORS, HandEnum.ROCK, True)
        assert_is_weaker_than_result(HandEnum.SCISSORS, HandEnum.PAPER, False)
        assert_is_weaker_than_result(HandEnum.SCISSORS, HandEnum.SCISSORS, False)

    def test_str(self) -> None:
        assert str(Hand.get_hand(HandEnum.ROCK)) == "Rock"
        assert str(Hand.get_hand(HandEnum.PAPER)) == "Paper"
        assert str(Hand.get_hand(HandEnum.SCISSORS)) == "Scissors"
