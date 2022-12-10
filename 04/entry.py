from __future__ import annotations  # クラス内で自分自身の型を参照するために必要
from typing import List
from abc import ABC, abstractmethod


class Entry(ABC):
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def get_children(self) -> List[Entry]:
        pass
