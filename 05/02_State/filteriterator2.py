from typing import Final, Iterator
from enum import Enum
from state import State, Context
from afterspace import AfterSpace


class FilterIterator2(Iterator[str], Context):
    _original: Iterator[str]

    def __init__(self, original: Iterator[str]) -> None:
        super().__init__()
        self._original = original

    _state: State = AfterSpace()

    def set_state(self, state: State):
        self._state = state

    def __next__(self) -> str:
        # ここで original から1文字取得して， ch に代入する
        ch = next(self._original)

        return self._state.process_char(self, ch)


if __name__ == "__main__":
    for ch in FilterIterator2(iter("The quick brown fox jumps over a lazy dull dog.\n")):
        print(ch, end="")
