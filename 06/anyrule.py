from rule import Rule
from command import Command
from message import Message


class AnyRule(Rule):
    def __init__(self, command: Command) -> None:
        super().__init__(command)

    def check(self, msg: Message) -> bool:
        return True
