from command import Command
from message import Message


class SaveCommand(Command):
    def run(self, msg: Message):
        print("Message from " + msg.sender + " saved.")
