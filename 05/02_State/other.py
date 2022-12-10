from __future__ import annotations
from state import Context, State
from typing import Optional


class Other(State):
    _instance: Optional[Other] = None

    @classmethod
    def get_instance(cls) -> Other:
        if cls._instance is None:
            cls._instance = Other()
        return cls._instance

    def process_char(self, c: Context, ch: str) -> str:
        # 相互 import によるエラーを避けるために，import 文をメソッド内に書く必要がある
        from afterspace import AfterSpace
        if ch.isspace():
            c.set_state(AfterSpace.get_instance())
            return ch
        return '.'
