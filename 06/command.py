from abc import ABC, abstractmethod
from message import Message


class Command(ABC):
    @abstractmethod
    def run(self, msg: Message) -> None:
        pass
