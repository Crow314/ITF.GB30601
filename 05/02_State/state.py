from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def process_char(self, f: Context, ch: str) -> str:
        pass


class Context(ABC):
    @abstractmethod
    def set_state(self, state: State):
        pass
