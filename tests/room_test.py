from src.room import *
from src.song import *
from src.guest import *
import unittest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("1", 0)
        self.guest_1 = Guest("Hansel", 20)
        self.song1 = Song("Can't take my eyes off you", "Frankie Valli")

    def test_find_room_number(self):
        self.assertEqual("1", self.room1.room_num)

    def test_empty_room(self):
        self.assertEqual(0, self.room1.time)

    def test_guest_check_in_number(self):
        self.room1.guest_check_in(self.guest_1)
        self.assertEqual(1, len(self.room1.people_list))
    
    # def test_checked_in_guest_name(self):
    #     self.room1.guest_check_in(self.guest_1)
    #     self.assertEqual("Hansel", self.room1.people_list[0])

    def test_guest_check_out(self):
        self.room1.guest_check_in(self.guest_1)
        self.room1.guest_check_out(self.guest_1)
        self.assertEqual(0, len(self.room1.people_list))

    def test_add_song_to_room_by_title(self):
        title_in_room = self.room1.add_song_to_list(self.song1.title)
        self.assertEqual("Can't take my eyes off you", title_in_room)

    def test_add_song_to_room_by_artist(self):
        artist_in_room = self.room1.add_song_to_list(self.song1.artist)
        self.assertEqual("Frankie Valli", artist_in_room)

    def test_count_song_list(self):
        add_song = self.room1.add_song_to_list(self.song1.artist)
        self.assertEqual(1, self.room1.count_song_list())
