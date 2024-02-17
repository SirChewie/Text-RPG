class Game:
    def __init__(self,players:dict):
        self.__turn = 1
        self.__players = players
    def start_game(self):
        # TODO: start the game.
        print("Game started!")
    def reset_game(self):
        # TODO: restart the game.
        print("Game restarted!")
    def get_turn(self):
        return self.__turn
    def get_players(self):
        return self.__players

def create_game(player1:object, player2:object):
    p1_id = player1.get_id()
    p2_id = player2.get_id()
    session_id = p1_id + p2_id 
    print(f"Game session: {session_id} started")
    g = Game({p1_id:player1,p2_id:player2})
    return g
