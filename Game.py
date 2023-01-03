import Player
import Space
import Railway
import Utility
import Property
import random
import os
import pickle

class Game():
    def __init__(self):
        self.current_player = 1
        self.players = [
                            Player.Player(1, "Gracz 1", 50000),
                            Player.Player(2, "Gracz 2", 50000),
                            Player.Player(3, "Gracz 3", 50000),
                            Player.Player(4, "Gracz 4", 50000),
                       ]

        self.board = [
                        Space.Space(1, "Start"),
                        Property.Property(2, "Ulica Konopacka", 60, 10),
                        Property.Property(3, "Ulica Stalowa", 60, 10),
                        Railway.Railway(4, "Dworzec Zachodni", 200),
                        Property.Property(5, "Ulica Radzyminska", 100, 15),
                        Property.Property(6, "Ulica Jagiellonska", 100, 15),
                        Property.Property(7, "Ulica Targowa", 120, 18),

                        Space.Space(8, "Bezplatny Parking"),
                        Utility.Utility(9, "Elektrownia", 150, 6),
                        Property.Property(10, "Ulica plowiecka", 140, 20),
                        Property.Property(11, "Ulica Marsa", 140, 20),
                        Property.Property(12, "Ulica Grochowska", 160, 24),
                        Railway.Railway(13, "Dworzec Gdanski", 200),
                        Property.Property(14, "Ulica Obozowa", 180, 27),
                        Property.Property(15, "Ulica Slowackiego", 180, 27),

                        Space.Space(16, "Bezplatny Parking"),
                        Property.Property(17, "Ulica Wolska", 200, 30),
                        Property.Property(18, "Ulica Mickieiwcza", 220, 33),
                        Property.Property(19, "Ulica Slowackiego", 220, 33),
                        Property.Property(20, "Plac Wilsona", 240, 36),
                        Railway.Railway(21, "Dworzec Centralny", 200),
                        Property.Property(22, "Ulica Swietokrzyska", 260, 39),
                        Property.Property(23, "Krakowskie Przedmiescie", 260, 39),

                        Space.Space(24, "Bezplatny Parking"),
                        Property.Property(25, "Nowy Swiat", 280, 42),
                        Property.Property(26, "Plac Trzech Krzyzy", 300, 45),
                        Property.Property(27, "Ulica Marszalkowska", 300, 45),
                        Property.Property(28, "Aleje Jerozolismkie", 320, 48),
                        Railway.Railway(29, "Dworzec Wschodni", 200),
                        Utility.Utility(30, "Wodociagi", 150, 5),
                        Property.Property(31, "Ulica Belwederska", 340, 53),
                        Property.Property(32, "Aleje Ujazdowskie", 370, 60),

                     ]

    def __PrintBoard(self):
        
        for i in range(len(self.board)):
            if i % 8 == 0:
                print("\n" + "=" * 41)
                print("|", end="")

            print(str(self.board[i].id).rjust(4) + "|", end="")
        print("\n" + "=" * 41)

        print(f"Pozycje graczy:\n")
        for p in self.players:
            print(f"{p.name}: {p.position}")
            
    
    def RollDice(self):
        first_r = random.randint(1, 6)
        second_r = random.randint(1, 6)
        return (first_r, second_r)

    def PlayerMove(self):
        roll = self.RollDice()
        move_amount = roll[0] + roll[1]
        curr_p = self.players[self.current_player - 1]

        print(f"Wylosowano { roll[0] } oraz { roll[1] }. Suma oczek wynosi { move_amount } \n")
        curr_p.Move(move_amount)
        curr_space = self.board[curr_p.position - 1]

        interact = curr_space.Interaction(curr_p, self.players) 
        # 1 - do kupienia / 2 - do budowania / 3 - pobierz czynsz

        if interact == 1:
            print(f"Znajdujesz sie na polu:  {curr_space.id}, {curr_space.name}")
            print("To pole nie posiada wlasciciela\nCzy chcesz je kupic?\n  1) Tak\n  2) Nie")
            odp = input("Wybor: ")
            if odp == '2':
                return

            if not curr_p.Pay(curr_space.price):
                print("Nie posiadasz wystarczajaco pieniedzy")
            else:
                curr_space.owner = curr_p.id
                print(f"Kupiono pole: {curr_space.name}")

        elif interact == 2:
            print(f"Znajdujesz sie na polu:  {curr_space.id}, {curr_space.name}\nJestes wlascicielem tego pola")
            print("Posiada ono hotel") if curr_space.hotel else print(f"Posiada ono { curr_space.house_number } domkow")

            print("Czy chcesz na nim budowac?\n 1) Tak\n 2) Nie")
            odp = input("Wybor: ")
            if odp == '2':
                return

            while True:
                try:
                    if not curr_space.hotel and curr_space.house_number == 4:
                        x = input("Czy chcesz wybudowac hotel?\n 1) Tak\n 2) Nie\nWybor: ")
                        if x == '2':
                            return
                        x = 1

                    else:
                        x = int(input("Ile domkow chcesz wybudowac: "))
                        if x + curr_space.house_number > 4 or x < 0:
                            print("Niepoprawna ilosc domkow")
                            continue

                    if not curr_p.Pay(curr_space.house_price * x):
                        print("Nie posiadasz wystarczajaco pieniedzy")
                        continue
                    else:
                        curr_space.owner = curr_p.id
                        if not curr_space.hotel and curr_space.house_number == 4:
                            print("Wybudowano hotel")
                            curr_space.hotel = True
                            curr_space.house_number = 0
                            return

                        print(f"Wybudowano {x} domkow")
                        curr_space.house_number += x
                        return
                except:
                    print("Niepoprawna wartosc")
                    continue
        

        elif interact == 3:
            owner_player = self.players[curr_space.owner - 1]
            amount_pay = curr_space.CountRent(owner_player, curr_p, self.board)
            print(f"Znajdujesz sie na polu:  {curr_space.id}, {curr_space.name}")
            print(f"Znajdujesz sie na polu: { owner_player.name }\nCzynsz wynosi: { amount_pay }")
            input()

            if not curr_p.Pay(amount_pay):
                print("Nie posiadasz wystarczajaco pieniedzy")
                return
            
            owner_player.GiveMoney(amount_pay)
            print(f"Zaplacono czynsz: { amount_pay }")



        else:
            print(interact)

    def PlayerTurn(self):
        odp = "_"

        while odp != '1':
            odp = "_"

            os.system("cls")
            
            self.__PrintBoard()
            print("\n\n")
            print( ("Tura: " + self.players[self.current_player - 1].name).rjust(30) )
            
            print("1) Rzuc koscmi")
            print("2) Wyswietl dane gracza")
            print("3) Wyswietl dane wybranego pola")
            print("4) Zapisz i zakoncz rozgrywke")

            while odp != '1' and odp != '2' and odp != '3' and odp != '4':
                odp = input("Wybor: ")

                if odp != '1' and odp != '2' and odp != '3' and odp != '4':
                    print("Niepoprawna wartosc!")

            if odp == '2':
                print(self.players[self.current_player - 1])
                input()

            elif odp == '3':
                option_ = input("Wybierz pole ktore chcesz wyswietlic: ")
                try:
                    print(self.board[int(option_) - 1])
                    input()
                except:
                    pass
            elif odp == '4':
                try:
                    with open('board.dat', 'wb') as plik:
                        pickle.dump(self.board, plik)
                    with open('player.dat', 'wb') as plik:
                        pickle.dump(self.players, plik)
                    with open('starting_player.dat', 'wb') as plik:
                        pickle.dump(self.current_player, plik)

                    print("Zapisano rozgrywke")

                except:
                    print("Wystapil blad przy zapisie")
                    

                return True


        self.PlayerMove()

        if self.current_player == 4:
            self.current_player = 1
        else:
            self.current_player += 1
        input()
        return False


         