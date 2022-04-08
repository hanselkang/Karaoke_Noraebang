import unittest
from src.bar import Bar


class TestBar(unittest.TestCase):

    def setUp(self):
        self.beer = Bar("Tennents", 10)
        self.wine = Bar("Red Wine", 15)

    def test_find_by_name(self):
        self.assertEqual("Tennents", self.beer.name)

    def test_find_by_price(self):
        self.assertEqual(15, self.wine.price)
