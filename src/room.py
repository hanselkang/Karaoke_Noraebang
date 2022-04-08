class Room:
    def __init__(self, input_number, time, capacity, cash):
        self.room_num = input_number
        self.time = 0
        self.people_list = []
        self.songs_list = []
        self.capacity = capacity
        self.cash = cash
        self.entrance_fee = 5

    def guest_check_in(self, guest):
        if  len(self.people_list) < self.capacity :
            self.people_list.append(guest)
        else:
            return "Room is full"

    def guest_check_out(self, guest):
        if len(self.people_list) > 0:
            self.people_list.remove(guest)

    def add_song_to_list(self, song1):
        self.songs_list.append(song1)
        return self.songs_list[0]

    def count_song_list(self):
        return len(self.songs_list)
