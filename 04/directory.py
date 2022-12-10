from __future__ import annotations

from typing import List
from entry import Entry
from subject import Subject, Observer


class Directory(Entry, Subject):
    _children: List[Entry]
    _observers: List[Observer[Directory]]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children = []
        self._observers = []

    def get_children(self) -> List[Entry]:
        return self._children

    def add(self, e: Entry) -> None:
        self._children.append(e)
        self.notify_observers()

    def add_observer(self, o: Observer[Directory]) -> None:
        self._observers.append(o)

    def notify_observers(self) -> None:
        for o in self._observers:
            o.update(self)
