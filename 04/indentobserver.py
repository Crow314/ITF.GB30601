from observer import Observer
from entry import Entry


class IndentObserver(Observer[Entry]):
    def print_entries(self, depth: int, e: Entry) -> None:
        for _ in range(depth):
            print("  ", end="")
        print(e.get_name())

        for child in e.get_children():
            self.print_entries(depth+1, child)

    def update(self, e: Entry) -> None:
        self.print_entries(0, e)
