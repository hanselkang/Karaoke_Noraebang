class Bar:
    def __init__(self,name):
        self.name = name
        self.stock = {}

    def stock_value(self):
        total = 0
        for drink in self.stock:
            total += (drink.price * self.stock[drink])
        return total