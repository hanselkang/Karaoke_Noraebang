import unittest
from src.guest import Guest
from src.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Hansel", 20, 50, "Can't take my eyes off you")
        self.room1 = Room("1", 0, 6, 100)

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
