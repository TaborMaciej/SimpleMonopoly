import Purchasable

class Utility(Purchasable.Purchasable):
    def __init__(self, id, name, price, multiplier):
        self.multiplier = multiplier
        self.owner = -1
        super().__init__(id, name, price)
       

    def __str__(self):
        return super().__str__() + f"\nMnoznik: { self.multiplier }"

    
    def CountRent(self, owner_player, curr_player, board):
        return curr_player.last_roll * self.multiplier


    def Interaction(self, player, player_list):
        if super().Interaction(player, player_list) == 1:
            return 1

        if self.owner == player.id:
            return f"Jestes wlascicielem tego pola";

        return 3
            


