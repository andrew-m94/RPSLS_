from player import Player
from human import Human
from robot import Robot
import random

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
        print('Welcome')

    def play_round(self):
        print('Please input the number of the Gesture you would like.')
        print('1.) Rock')
        print('2.) Paper')
        print('3.) Scissors')
        print('4.) Lizard')
        print('5.) Spock')
        user_input1 = int(input(f'{self.players[0].name} Insert number here: '))
        self.players[0].pick_gesture(user_input1)
        user_input2 = int(input(f'{self.players[1].name} Insert number here'))
        self.players[1].pick_gesture(user_input2)
        self.compare_gesture(self.players[0].current_pick, self.players[1].current_pick)
        

    def choose_game_mode(self):
        user_input = input('Would you like to play Singleplayer or Multiplayer: ').lower()
        if user_input == 'singleplayer':
            self.add_player_and_ai()
        elif user_input == 'multiplayer':
            self.add_players()   

    def compare_gesture(self, p1_pick, p2_pick):
        compare_gesture = [[0, -1, 1, 1, -1],
                           [1, 0, -1, -1, 1],
                           [-1, 1, 0, 1, -1],
                           [-1, 1, -1, 0, 1],
                           [1, -1, 1, -1, 0]]

        winner = compare_gesture[p1_pick][p2_pick] 
        if winner == -1:
            print(f'{self.players[1].name} has won this round!')
            self.players[1].score += 1
        elif winner == 0:
            print('This round is a tie!')
        elif winner == 1:
            print(f'{self.players[0].name} has won this round!')
            self.players[0].score += 1        

    def display_winner(self):
        pass

    def run_game(self):
        self.welcome_message()
        self.choose_game_mode()
        self.play_round()
  