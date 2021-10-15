from player import Player

class Human(Player):
    def __init__(self):
        self.name = self.get_name()
        super().__init__(self)

    def get_name(self):
        user_input = input('Please insert your name here: ')
        self.name = user_input
