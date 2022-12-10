from message import Message
from savecommand import SaveCommand
from discardcommand import DiscardCommand
from printcommand import PrintCommand
from rule import Rule
from anyrule import AnyRule
from senderrule import SenderRule

if __name__ == '__main__':
    rule: Rule
    # ここでルールを組み立てる．

    rule1 = SenderRule(SaveCommand(), "alice")
    rule2 = SenderRule(DiscardCommand(), "bob")
    rule3 = AnyRule(PrintCommand())

    rule = rule1
    rule.set_next(rule2).set_next(rule3)

    msgs = [
        Message("alice", "me", "Hello, this is Alice."),
        Message("bob", "me", "Hello from Bob."),
        Message("charlie", "me", "Hi, it's Charlie.")
    ]

    for m in msgs:
        # ここでメッセージmについてルールを実行する．
        rule.handle(m)
