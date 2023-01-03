import Purchasable

class Railway(Purchasable.Purchasable):
    def __init__(self, id, name, price):
        self.rent = 50
        self.owner = -1
        super().__init__(id, name, price)

    def __str__(self):
        return super().__str__() + f"\nCzynsz podstawowy: { self.rent }"
           
    def CountRent(self, owner_player, curr_player, board):
        count = 0
        for space_ in board:
            try:
                if space_.owner == owner_player.id and type(space_).__name__ == "Railway":
                    count += 1
            except:
                continue
        return self.rent * count
    
    def Interaction(self, player, player_list):
        if super().Interaction(player, player_list) == 1:
            return 1

        if self.owner == player.id:
            return f"Znajdujesz sie na polu:  {self.id}, {self.name}\nJestes wlascicielem tego pola";

        return 3
            


