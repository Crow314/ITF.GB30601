from typing import List
from entry import Entry


class File(Entry):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_children(self) -> List[Entry]:
        return []
