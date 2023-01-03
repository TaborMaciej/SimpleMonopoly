import Space

class Purchasable(Space.Space):

    def __init__(self, id, nazwa, price):
        self.price = price
        self.owner = -1
        super().__init__(id, nazwa)

    def __str__(self):
        if self.owner == -1:
            owner_msg = "Brak wlasciciela"
        else:
            owner_msg = f"Gracz {self.owner}"

        return super().__str__() + f"\nCena: { self.price }\nWlasciciel: { owner_msg}"

    def Interaction(self, player, player_list):
        if self.owner == -1:
            return 1