import unittest
from src.drink import Drink
from src.bar import Bar
from src.guest import Guest


class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Beer", 5)

    def test_drink_nam(self):
        self.assertEqual("Beer", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(5, self.drink.price)
