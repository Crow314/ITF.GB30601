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

#     def __iter__(self) -> Iterator[Book]:
#         return BookShelfIterator(self)


# class BookShelfIterator(Iterator[Book]):
#     def __init__(self, book_shelf: BookShelf) -> None:
#         self.book_shelf: BookShelf = book_shelf
#         self._index: int = 0
#
#     def __next__(self) -> Book:
#         if self._index >= len(self.book_shelf):
#             raise StopIteration
#
#         result = self.book_shelf.book_at(self._index)
#         self._index += 1
#         return result
