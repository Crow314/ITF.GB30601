from observer import Observer
from entry import Entry


class CountingObserver(Observer[Entry]):
    def count_entries(self, e: Entry) -> int:
        """ 木構造eの中のEntryの数を返す． """
        count: int = 1
        for child in e.get_children():
            count += self.count_entries(child)
        return count

    def update(self, e: Entry) -> None:
        print(e.get_name() + " contains " + str(self.count_entries(e)) + " entries.")
