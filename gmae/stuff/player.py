#classes for player

class Player:
    'Base for player'

    playercount = 0

    def __init__(self, name):
        self.name = name
        Player.playercount += 0