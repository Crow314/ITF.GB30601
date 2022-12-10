from typing import Final, Iterator
from enum import Enum


class FilterIterator(Iterator[str]):
    _original: Iterator[str]

    def __init__(self, original: Iterator[str]) -> None:
        super().__init__()
        self._original = original

    AFTER_SPACE: Final[int] = 1
    OTHER: Final[int] = 2

    _state: int = AFTER_SPACE

    def set_state(self, new_state: int):
        self._state = new_state

    def __next__(self) -> str:
        # ここで original から1文字取得して， ch に代入する
        ch = next(self._original)

        if self._state == FilterIterator.AFTER_SPACE:
            if not ch.isspace():
                self.set_state(FilterIterator.OTHER)
            return ch
        else:
            if ch.isspace():
                self.set_state(FilterIterator.AFTER_SPACE)
                return ch
            return '.'


if __name__ == "__main__":
    for ch in FilterIterator(iter("The quick brown fox jumps over a lazy dull dog.\n")):
        print(ch, end="")
