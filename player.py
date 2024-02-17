
# TODO: Make general "in-game race" Class
class Race:
    """In-game race"""
    def __init__(self):
        self.__racal_bonus = "Racal Bonus!!!"

# TODO: Make general "in-game class" Class
class Role:
    """In-game role"""
    def __init__(self,role):
        self.__role = ("Class:",f"{role}")
    def get_role(self):
        return self.__role


class Player(Role, Race):
    """ The player object\n
Inheritances:\n(Role -> Player)\n(Race -> Player)\n
    """
    def __init__(self,name,role,player_num):
        super().__init__(role)
        self.__name = ("name",name)
        self.__id = f"{name}_{player_num}"
        self.__level = ("level",1)
        self.__health = ("health",0)
        self.__dmg = ("dmg",1)
        self.__stats = {}
        self.set_stats()

    def set_stats(self):
        l = [
            self.get_name(),
            self.get_role(),
            self.get_level(),
            self.get_health(),
            self.get_dmg(),
        ]
        for name,stat in l:
            self.__stats[name] = stat

    def get_stats(self):
        return self.__stats
    def get_name(self):
        return self.__name
    def get_level(self):
        return self.__level
    def get_health(self):
        return self.__health
    def get_dmg(self):
        return self.__dmg
    def get_id(self):
        return self.__id
    

def create_player():
    player_num = 0
    def player_create():
        nonlocal player_num
        name = input("Character name:\n")
        role = "Warrior"
        p = Player(name,role,player_num)
        player_num += 1
        return p
    return player_create