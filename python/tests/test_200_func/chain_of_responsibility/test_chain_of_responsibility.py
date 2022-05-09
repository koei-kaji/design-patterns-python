import pytest

from src.chain_of_responsibility.limit_support import LimitSupport
from src.chain_of_responsibility.no_support import NoSupport
from src.chain_of_responsibility.odd_support import OddSupport
from src.chain_of_responsibility.special_support import SpecialSupport
from src.chain_of_responsibility.trouble import Trouble


class TestSupport:
    @pytest.mark.parametrize(("exec_recursively"), [(True), (False)])
    def test_normal(self, exec_recursively: bool) -> None:
        spt_alice = NoSupport(name="Alice")
        spt_bob = LimitSupport(name="Bob", limit=100)
        spt_charlie = SpecialSupport(name="Charlie", number=429)
        spt_diana = LimitSupport(name="Diana", limit=200)
        spt_elmo = OddSupport(name="Elmo")
        spt_fred = LimitSupport(name="Fred", limit=300)

        spt_alice.set_next(spt_bob).set_next(spt_charlie).set_next(spt_diana).set_next(
            spt_elmo
        ).set_next(spt_fred)

        # TODO: テストが面倒なのでとりあえず標準出力
        print("")
        for i in range(0, 500, 33):
            spt_alice.support(Trouble(number=i), exec_recursively=exec_recursively)
