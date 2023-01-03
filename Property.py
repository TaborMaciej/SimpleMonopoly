import Purchasable

class Property(Purchasable.Purchasable):
    def __init__(self, id, nazwa, price, rent):
        self.rent = rent
        self.house_number = 0
        self.hotel = False
        self.house_price = 150
        super().__init__(id, nazwa, price)
       

    def __str__(self):
        if self.hotel:
            house = "Wybudowano hotel"
        else:
            house = "Ilosc domkow: " + str(self.house_number)
        return super().__str__() + f"\nCzynsz: { self.CountRent(0, 0, 0) }\n{ house }"

    def CountRent(self, owner_player, curr_player, board):
        if self.hotel:
            return self.rent + 200
        return self.rent + self.house_number * 30

    def Interaction(self, player, player_list):
        if super().Interaction(player, player_list) == 1:
            return 1

        if self.owner == player.id:
            if self.hotel:
                return f"Jestes wlascicielem tego pola. Jest ono w pelni zabudowane";

            return 2

        return 3
            


