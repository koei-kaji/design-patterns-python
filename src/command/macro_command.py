from typing import List

from pydantic import BaseModel, PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from .command import CommandIF


class MacroCommand(BaseModel, CommandIF):
    _commands: List[CommandIF] = PrivateAttr(default=[])

    def execute(self) -> None:
        for command in self._commands:
            command.execute()

    def append(self, command: CommandIF) -> None:
        if command == self:
            return

        self._commands.append(command)

    def undo(self) -> None:
        if self._commands == []:
            return

        del self._commands[-1]

    def clear(self) -> None:
        self._commands.clear()

    class Config(BaseFrozenConfig):
        pass
