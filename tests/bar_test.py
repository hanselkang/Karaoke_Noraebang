import unittest
from src.bar import Bar
from src.drink import Drink
from src.guest import Guest
from src.room import Room


class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("bar_caraoke")
        self.drink = Drink("Beer", 5)
        self.guest_1 = Guest("Hansel", 20, 50, "Can't take my eyes off you")
        self.room1 = Room("1", 0, 6, 100)

    def test_bar_name(self):
        self.assertEqual("bar_caraoke",self.bar.name )

    def test_add_drink(self):
        self.bar.add_drink(self.drink)
        self.assertEqual(1, self.bar.stock_level(self.drink))
        self.assertEqual(5, self.bar.stock_value())
    
    def test_bar_stock_value_0(self):
        self.assertEqual(0, self.bar.stock_value())

    def test_bar_can_add_multiple_drink(self):
        self.bar.add_drink(self.drink)
        self.bar.add_drink(self.drink)
        self.assertEqual(2, self.bar.stock_level(self.drink))
        self.assertEqual(10, self.bar.stock_value())

    def test_cannot_serve(self):
        self.assertEqual(False,  self.bar.can_serve(self.guest_1, self.drink))

    def test_old_enough(self):
        self.assertEqual(True,self.bar.guest_challenge25(self.guest_1))