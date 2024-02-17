from game import Game, create_game
from player import Player, create_player
from server.serve import start_server

def main():
    start_server(HOST='',PORT=25565)
    print("Connecting successful")
    new_player = create_player()
    p1 = new_player()
    p2 = new_player()
    g = create_game(p1,p2)
    print(g.get_turn())
    print(g.get_players())

if __name__ == "__main__":
    while True:
        main()
