import unittest
from src.bar import Bar
from src.drink import Drink
from src.guest import Guest


class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("bar_caraoke")
        self.drink = Drink("Beer", 5)
        self.guest_1 = Guest("Hansel", 20, 50, "Can't take my eyes off you")

    def test_bar_name(self):
        self.assertEqual("bar_caraoke",self.bar.name )
    
    def test_bar_stock_value_0(self):
        self.assertEqual(0, self.bar.stock_value())