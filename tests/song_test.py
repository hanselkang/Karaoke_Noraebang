from src.song import *
import unittest


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Can't take my eyes off you")

    def test_find_song_by_name(self):
        self.assertEqual("Can't take my eyes off you",self.song1.name)
