class Bar:
    def __init__(self,name):
        self.name = name
        self.stock = {}

    def add_drink(self, drink):
        if drink in self.stock:
            self.stock[drink] += 1
        else:
            self.stock[drink] = 1
    
    def stock_level(self, drink):
        if  drink in self.stock:
            return self.stock[drink]
        else:
            return 0

    def stock_value(self):
        total = 0
        for drink in self.stock:
            total += (drink.price * self.stock[drink])
        return total