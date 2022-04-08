from src.room import Room


class Guest:
    def __init__(self, input_name, input_age, input_budget):
        self.name = input_name
        self.age = input_age
        self.budget = input_budget

    def pay_fee(self, fee):
        self.budget -= fee
        
