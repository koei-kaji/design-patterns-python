from __future__ import annotations

import abc
from typing import List, Union

from pydantic import PrivateAttr

from ..common.custom_pydantic.config import BaseFrozenConfig
from ..common.custom_pydantic.model import ABCModel
from .context import Context
from .exc import ParseException


class NodeABC(ABCModel):
    @abc.abstractmethod
    def parse(self, context: Context) -> None:
        pass


# <program> ::= program <command list>
class ProgramNode(NodeABC):
    _command_list_node: CommandListNode = PrivateAttr()

    def parse(self, context: Context) -> None:
        context.skip_token("program")
        self._command_list_node = CommandListNode()
        self._command_list_node.parse(context)

    def __str__(self) -> str:
        return f"[program {self._command_list_node}]"

    class Config(NodeABC.Config, BaseFrozenConfig):
        pass


# <command list> ::= <command>* end
class CommandListNode(NodeABC):
    _command_nodes: List[CommandNode] = PrivateAttr(default=[])

    def parse(self, context: Context) -> None:
        while True:
            if context.current_token() is None:
                raise ParseException("Missing 'end'")
            elif context.current_token() == "end":
                context.skip_token("end")
                break
            else:
                command_node = CommandNode()
                command_node.parse(context)
                self._command_nodes.append(command_node)

    def __str__(self) -> str:
        return self._command_nodes.__str__()

    class Config(NodeABC.Config, BaseFrozenConfig):
        pass


# <command> ::= <repeat command> | <primitive command>
class CommandNode(NodeABC):
    _node: Union[RepeatCommandNode, PrimitiveCommandNode] = PrivateAttr()

    def parse(self, context: Context) -> None:
        if context.current_token() == "repeat":
            self._node = RepeatCommandNode()
        else:
            self._node = PrimitiveCommandNode()
        self._node.parse(context)

    def __str__(self) -> str:
        return self._node.__str__()

    def __repr__(self) -> str:
        return self._node.__str__()

    class Config(NodeABC.Config, BaseFrozenConfig):
        pass


# <repeat command> ::= repeat <number> <command list>
class RepeatCommandNode(NodeABC):
    _number: int = PrivateAttr()
    _command_list_node: CommandListNode = PrivateAttr()

    def parse(self, context: Context) -> None:
        context.skip_token("repeat")
        self._number = context.current_number()
        context.next_token()
        self._command_list_node = CommandListNode()
        self._command_list_node.parse(context)

    def __str__(self) -> str:
        return f"[repeat {self._number} {self._command_list_node}]"

    class Config(NodeABC.Config, BaseFrozenConfig):
        pass


# <primitive command> ::= go | right | left
class PrimitiveCommandNode(NodeABC):
    _name: str = PrivateAttr()

    def parse(self, context: Context) -> None:
        current_token = context.current_token()
        if current_token is None:
            raise ParseException("current_token is None")
        context.skip_token(current_token)
        if current_token not in ["go", "right", "left"]:
            raise ParseException(f"{self._name} is undefined")

        self._name = current_token

    def __str__(self) -> str:
        return self._name

    class Config(NodeABC.Config, BaseFrozenConfig):
        pass
