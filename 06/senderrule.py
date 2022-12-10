from rule import Rule
from command import Command
from message import Message


class SenderRule(Rule):
    _sender: str

    def __init__(self, command: Command, sender: str) -> None:
        super().__init__(command)
        self._sender = sender

    def check(self, msg: Message) -> bool:
        return msg.sender == self._sender
