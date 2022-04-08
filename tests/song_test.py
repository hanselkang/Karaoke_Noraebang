from src.song import *
import unittest


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Can't take my eyes off you", "Frankie Valli")

    def test_find_song_by_title(self):
        self.assertEqual("Can't take my eyes off you",self.song1.title)

    def test_find_song_by_artist(self):
        self.assertEqual("Frankie Valli", self.song1.artist)
