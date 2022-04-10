import unittest
from src.guest import Guest
from src.room import Room
from src.drink import Drink


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Hansel", 20, 50, "Can't take my eyes off you")
        self.guest_2 = Guest("Billy", 20, 4, "Only You")
        self.room1 = Room("1", 0, 6, 100)
        self.drink = Drink("Beer", 5)

    def test_guest_name(self):
        self.assertEqual("Hansel", self.guest_1.name)

    def test_guest_age(self):
        self.assertEqual(20, self.guest_1.age)

    def test_how_much_guest_has(self):
        self.assertEqual(50, self.guest_1.budget)

    def test_pay_fee(self):
        self.guest_1.pay_fee(self.room1.entrance_fee)
        self.assertEqual(45, self.guest_1.budget)

    def test_fav_song(self):
        self.assertEqual("Can't take my eyes off you", self.guest_1.fav_song)

    def test_favourite_song(self):
        self.assertEqual(
            "Wooohooo!", self.guest_1.fav_song_play(self.guest_1.fav_song))

    def test_sufficient_funds__true(self):
        self.assertEqual(True, self.guest_1.sufficient_funds(self.drink))

    def test_sufficient_funds__False(self):
        self.assertEqual(False, self.guest_2.sufficient_funds(self.drink))

    def test_buy_a_drink(self):
        self.guest_1.buy_drink(self.drink)
        self.assertEqual(45, self.guest_1.budget)
