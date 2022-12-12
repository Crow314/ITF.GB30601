from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod
from typing import Optional


def play_sound(path: str):
    global WORKDIR

    # subprocess.Popen(['aplay', WORKDIR + path])
    print('Play' + path)


class InOutState(ABC):
    @abstractmethod
    def pass_gate(self, c: InOutContext, name: str):
        pass


class InOutContext(ABC):
    @abstractmethod
    def set_state(self, state: InOutState):
        pass


class InState(InOutState):
    _instance: Optional[InState] = None

    @classmethod
    def get_instance(cls) -> InState:
        if cls._instance is None:
            cls._instance = InState()
        return cls._instance

    def pass_gate(self, c: InOutContext, name: str) -> str:
        c.set_state(OutState.get_instance())
        play_sound('/out/sayonara.wav')
        return name + 'が退出しました'


class OutState(InOutState):
    _instance: Optional[OutState] = None

    @classmethod
    def get_instance(cls) -> OutState:
        if cls._instance is None:
            cls._instance = OutState()
        return cls._instance

    def pass_gate(self, c: InOutContext, name: str) -> str:
        c.set_state(InState.get_instance())
        play_sound('/in/okaeri.wav')
        return name + 'が入室しました'
