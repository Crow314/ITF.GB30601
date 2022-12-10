import unittest
from book import Book
from bookshelf import BookShelf


class BookShelfTest(unittest.TestCase):
    def setUp(self):
        self.bs = BookShelf()
        self.b1 = Book("a1", "t1")
        self.b2 = Book("a2", "t2")
        self.b3 = Book("a3", "t3")

        self.bs.append_book(self.b1)
        self.bs.append_book(self.b2)
        self.bs.append_book(self.b3)

    def test_len(self):
        self.assertEqual(len(self.bs), 3)

    def test_iterator(self):
        i = iter(self.bs)

        b = next(i)
        self.assertEqual(b, self.b1)

        b = next(i)
        self.assertEqual(b, self.b2)

        b = next(i)
        self.assertEqual(b, self.b3)

    def test_remove_at(self):
        # Step 1
        self.bs.remove_at(1)

        # Step 2
        self.assertEqual(len(self.bs), 2)

        # Step 3
        self.assertEqual(self.bs.book_at(0), self.b1)
        self.assertEqual(self.bs.book_at(1), self.b3)

        # Step 4
        self.bs.remove_at(0)
        self.bs.remove_at(0)

        # Step 5
        self.assertEqual(len(self.bs), 0)
