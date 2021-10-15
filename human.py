from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(self)