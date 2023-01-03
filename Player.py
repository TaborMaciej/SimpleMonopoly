
class Player():
    def __init__(self, id, name, money):
        self.id = id
        self.name = name
        self.money = money
        self.position = 1
        self.last_roll = -1

    def __str__(self):
        return f"{ '=' * (len(self.name) + 6) }\n   {self.name}   \n{ '=' * (len(self.name) + 6) }\nID: {self.id}\nIlosc pieniedzy: {self.money}"

    def Pay(self, amount):
        if self.money < amount:
            return False
        if self.money >= amount:
            return True

    def GiveMoney(self, amount):
        self.money += amount

    def Move(self, amount):
        self.last_roll = amount
        self.position += amount
        if self.position > 32:
            self.position -= 32
