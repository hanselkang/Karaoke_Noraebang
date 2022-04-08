from src.room import Room
from src.drink import Drink


class Guest:
    def __init__(self, input_name, input_age, input_budget, fav_song):
        self.name = input_name
        self.age = input_age
        self.budget = input_budget
        self.fav_song = fav_song

    def pay_fee(self, fee):
        self.budget -= fee

    def fav_song_play(self, song):
        if song == self.fav_song:
            return "Wooohooo!"

    def sufficient_funds(self, beer):
        return self.budget >= beer.price

    def buy_drink(self, guest, drink):
        return self.budget - drink.price