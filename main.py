import Game
import pickle



print("1) Nowa gra")
print("2) Wczytaj poprzednia gre")
odp = "_"
while odp != '1' and odp != '2':
    odp = input("Wybor: ")
    
stopped = False
game_ = Game.Game()

if odp == '2':
    with open('board.dat', 'rb') as plik:
            print("board")
            board = pickle.load(plik)
    try:
        with open('board.dat', 'rb') as plik:
            print("board")
            board = pickle.load(plik)

        with open('player.dat', 'rb') as plik:
            print("board2")
            players = pickle.load(plik)

        with open('starting_player.dat', 'rb') as plik:
            print("board3")
            current_player = pickle.load(plik)

        game_.board = board
        game_.players = players
        game_.current_player = current_player

    except:
        print("Wystapil blad przy wczytywaniu rozgrywki")
        stopped = True


while not stopped:
    stopped = game_.PlayerTurn()
