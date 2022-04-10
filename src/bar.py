from src.room import Room
from src.guest import Guest


class Bar:
    def __init__(self, name):
        self.name = name
        self.stock = {}

    def add_drink(self, drink):
        if drink in self.stock:
            self.stock[drink] += 1
        else:
            self.stock[drink] = 1

    def stock_level(self, drink):
        if drink in self.stock:
            return self.stock[drink]
        else:
            return 0

    def stock_value(self):
        total = 0
        for drink in self.stock:
            total += (drink.price * self.stock[drink])
        return total

    def customer_can_afford_drink(self, customer, drink):
        return customer.sufficient_funds(drink)

    def guest_challenge25(self, guest):
        return guest.age >= 18

    def can_serve(self, guest, drink):
        if not self.guest_challenge25(guest):
            return False
        if self.stock_level(drink) == 0:
            return False
        return True


