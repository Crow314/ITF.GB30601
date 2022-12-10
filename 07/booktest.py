import unittest
from book import Book


class BookTest(unittest.TestCase):
    def test_author(self):
        b = Book("a", "b")
        self.assertEqual(b.author, "a")
