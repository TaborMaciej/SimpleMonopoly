class Space():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{ '=' * (len(self.name) + 6) }\n   {self.name}   \n{ '=' * (len(self.name) + 6) }\nID: {self.id}"

    def Interaction(self, player, player_list):
        return f"Znajdujesz sie na polu:  {self.id}, {self.name}"
        