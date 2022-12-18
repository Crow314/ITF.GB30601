import unittest
from person import Person


class PersonTest (unittest.TestCase):
    def test_office_telephone_number(self):
        p = Person('name', 'company', '029', '853-2319')

        self.assertEqual(p.office_telephone_number, "029-853-2319")
