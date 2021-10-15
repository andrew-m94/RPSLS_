from player import Player
from human import Human
from robot import Robot

class PlayArea:
    def __init__(self):
        self.gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.max_score = 2
        self.players = []

    def add_players(self):
        player_one = Human()
        player_two = Human()
        self.players.append(player_one)
        self.players.append(player_two)

    def add_player_and_ai(self):
        player_one = Human()
        player_two = Robot()
        self.players.append(player_one)
        self.players.append(player_two)

    def welcome_message(self):
        pass

    def choose_game_mode(self):
        user_input = input('Would you like to play Singleplayer or Multiplayer: ').lower()
        if user_input == 'singleplayer':
            self.add_player_and_ai()
        elif user_input == 'multiplayer':
            self.add_players()    

    def display_winner(self):
        pass

    def run_game(self):
        pass