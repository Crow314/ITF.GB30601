from book import Book
from typing import Iterable, Iterator, List


class BookShelf(Iterable[Book]):
    _books: List[Book]

    def __init__(self) -> None:
        self._books = []

    def book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books.append(book)

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self) -> Iterator[Book]:
        for book in self._books:
            yield book

    def remove_at(self, index: int):
        self._books.pop(index)
