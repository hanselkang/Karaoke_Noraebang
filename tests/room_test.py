from src.room import *
import unittest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("1",0)

    def test_find_room_number(self):
        self.assertEqual("1",self.room1.room_num)

    def test_empty_room(self):
        self.assertEqual(0, self.room1.time)