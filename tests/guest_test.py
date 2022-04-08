import unittest
from src.guest import Guest



class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Hansel", 20)

    def test_guest_name(self):
        self.assertEqual("Hansel", self.guest_1.name)

    def test_guest_age(self):
        self.assertEqual(20, self.guest_1.age)
