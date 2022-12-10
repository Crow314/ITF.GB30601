from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from observer import Observer

E = TypeVar('E')


class Subject(ABC, Generic[E]):
    @abstractmethod
    def add_observer(self, o: Observer[E]) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass
