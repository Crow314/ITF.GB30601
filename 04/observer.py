from abc import ABC, abstractmethod
from typing import Generic, TypeVar

E = TypeVar('E')


class Observer(ABC, Generic[E]):
    @abstractmethod
    def update(self, e: E) -> None:
        pass
