from typing import Iterable, Iterator


class Range(Iterable[int]):
    _from: int
    _to: int
    _step: int

    def __init__(self, from_: int, to: int, step: int = 1) -> None:
        # stepを略すと，1を指定した扱いにする
        self._from = from_
        self._to = to
        self._step = step

    def __iter__(self) -> Iterator[int]:
        return RangeIterator(self)

    def __iter2__(self) -> Iterator[int]:
        v = self._from
        while v < self._to:
            yield v
            v += self._step


class RangeIterator(Iterator[int]):
    _r: Range
    _i: int

    def __init__(self, range: Range) -> None:
        self._r = range
        self._i = range._from

    def __next__(self) -> int:
        v = self._i
        if v > self._r._to:
            raise StopIteration

        self._i += self._r._step
        return v


if __name__ == "__main__":
    # 1から10未満まで，2おきに繰り返す
    r = Range(1, 10, 2)
    for v in r:
        print(v)
    print("----")
    r2 = Range(1, 5)
    for v in r2:
        print(v)