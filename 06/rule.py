from __future__ import annotations
from abc import ABC, abstractmethod
from typing import final, Optional
from message import Message
from command import Command


class Rule(ABC):
    _command: Command
    _next: Optional[Rule]

    def __init__(self, command: Command) -> None:
        self._command = command
        self._next = None

    @abstractmethod
    def check(self, msg: Message) -> bool:
        pass

    @final
    def set_next(self, next: Rule) -> Rule:
        self._next = next
        return next

    @final
    def handle(self, msg: Message) -> None:
        if self.check(msg):
            self._command.run(msg)
        elif self._next is not None:
            self._next.handle(msg)
