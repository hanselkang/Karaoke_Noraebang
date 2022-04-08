from src.room import *
from src.song import *
from src.guest import *
import unittest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("1", 0, 6)
        self.guest_1 = Guest("Hansel", 20)
        self.guest_2 = Guest("Abdul", 24)
        self.guest_3 = Guest("Bryan", 21)
        self.guest_4 = Guest("Charles", 28)
        self.guest_5 = Guest("David", 29)
        self.guest_6 = Guest("Emily", 24)
        self.guest_7 = Guest("Frankie", 30)
        self.guest_group = [self.guest_1,
                            self.guest_2, self.guest_3, self.guest_4, self.guest_5, self.guest_6]
        self.song1 = Song("Can't take my eyes off you", "Frankie Valli")

    def test_find_room_number(self):
        self.assertEqual("1", self.room1.room_num)

    def test_empty_room(self):
        self.assertEqual(0, self.room1.time)

    def test_guest_check_in_number(self):
        self.room1.guest_check_in(self.guest_1)
        self.assertEqual(1, len(self.room1.people_list))

    def test_checked_in_guest_name(self):
        self.room1.guest_check_in(self.guest_1)
        self.assertEqual("Hansel", self.room1.people_list[0].name)

    def test_checked_in_guest_age(self):
        self.room1.guest_check_in(self.guest_1)
        self.assertEqual(20, self.room1.people_list[0].age)

    def test_guest_check_out(self):
        self.room1.guest_check_in(self.guest_1)
        self.room1.guest_check_out(self.guest_1)
        self.assertEqual(0, len(self.room1.people_list))

    def test_add_song_to_room_by_title(self):
        self.room1.add_song_to_list(self.song1)
        self.assertEqual("Can't take my eyes off you",
                         self.room1.songs_list[0].title)

    def test_add_song_to_room_by_artist(self):
        self.room1.add_song_to_list(self.song1)
        self.assertEqual("Frankie Valli", self.room1.songs_list[0].artist)

    def test_count_song_list(self):
        add_song = self.room1.add_song_to_list(self.song1)
        self.assertEqual(1, self.room1.count_song_list())

    def test_if_the_room_is_full(self):
        for people in self.guest_group:
            self.room1.guest_check_in(people)
        self.assertEqual(
            "Room is full", self.room1.guest_check_in(self.guest_7))
