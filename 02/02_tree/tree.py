from __future__ import annotations
from typing import Iterable, Iterator, List, Optional


class Tree(Iterable['Tree']):
    _label: str
    _left: Optional[Tree]
    _right: Optional[Tree]

    def __init__(self, label: str, left: Optional[Tree], right: Optional[Tree]) -> None:
        self._label = label
        self._left = left
        self._right = right

    def __iter__(self) -> Iterator[Tree]:
        return _TreeIterator(self)


class _TreeIterator(Iterator[Tree]):
    _stack: List[Tree]

    def __init__(self, tree: Tree) -> None:
        self._stack = []
        self._stack.append(tree)  # 木の根だけpushしておく．

    def __next__(self) -> Tree:
        if len(self._stack) == 0:
            raise StopIteration

        node = self._stack.pop()   # これから調べるノードをpopする．

        #  ここに，子供があれば，将来nextが呼ばれた時に調べるようpushするよう追記する
        if node._right:
            self._stack.append(node._right)
        if node._left:
            self._stack.append(node._left)

        return node         # 最初にpopしたノードを返す．
