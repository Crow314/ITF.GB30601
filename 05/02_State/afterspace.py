from __future__ import annotations
from state import Context, State
from typing import Optional


class AfterSpace(State):
    _instance: Optional[AfterSpace] = None

    @classmethod
    def get_instance(cls) -> AfterSpace:
        if cls._instance is None:
            cls._instance = AfterSpace()
        return cls._instance

    def process_char(self, c: Context, ch: str) -> str:
        # 相互 import によるエラーを避けるために，import 文をメソッド内に書く必要がある
        from other import Other
        if not ch.isspace():
            c.set_state(Other.get_instance())
        return ch
