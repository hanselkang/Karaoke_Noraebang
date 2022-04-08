class Room:
    def __init__(self, input_number, time):
        self.room_num = input_number
        self.time = 0
        self.people_list = []
        self.songs_list = []

    def guest_check_in(self, guest):
        self.people_list.append(guest)

    def guest_check_out(self, guest):
        self.people_list.remove(guest)

    # def add_song_to_list(self, name):
    #     self.songs_list.append(name)
    #     return self.songs_list[0]