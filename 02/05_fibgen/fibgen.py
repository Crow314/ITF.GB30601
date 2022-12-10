class FibGenerator:
    _num: int
    _i: int
    _j: int

    def __init__(self, num: int):
        self._num = num
        self._i = 0
        self._j = 1

    def __iter__(self):
        for _ in range(self._num):
            yield self._j

            tmp = self._j
            self._j = self._i + tmp
            self._i = tmp


if __name__ == "__main__":
    for v in FibGenerator(10):
        print(v)
