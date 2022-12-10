from command import Command
from message import Message


class DiscardCommand(Command):
    def run(self, msg: Message) -> None:
        print("Message from " + msg.sender + " discarded.")
