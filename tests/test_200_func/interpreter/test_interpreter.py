from pathlib import Path
from typing import Final

from src.interpreter.context import Context
from src.interpreter.node import NodeABC, ProgramNode

DIR_BASE: Final[Path] = Path(__file__).parent
PROGRAM_FILE_PATH: Final[Path] = DIR_BASE / "program.txt"


class TestNode:
    def test_normal(self) -> None:
        with open(PROGRAM_FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                print(f"text = {line}")
                node: NodeABC = ProgramNode()
                node.parse(Context(text=line))
                print(f"node = {node}")
