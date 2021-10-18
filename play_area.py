from player import Player
from human import Human
from robot import Robot
from gestures import Gestures
import random

class PlayArea:
    def __init__(self):
        self.gesture_list = []
        self.max_score = 2
        self.players = []
        self.add_gestures()

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

    def add_gestures(self):
        rock = Gestures('Rock')
        self.gesture_list.append(rock)

        paper = Gestures('Paper')
        self.gesture_list.append(paper)

        scissors = Gestures('Scissors')
        self.gesture_list.append(scissors)

        lizard = Gestures('Lizard')
        self.gesture_list.append(lizard)

        spock = Gestures('Spock')
        self.gesture_list.append(spock)

    def welcome_message(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!\n')
        print('The rules are as follows:')
        print(f'Rock crushes Scissors\nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard' +
         '\nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard\n')

    def play_round(self):
        print('Please input the number of the Gesture you would like.')
        print('1.) Rock ✊')
        print('2.) Paper 🤚')
        print('3.) Scissors ✌')
        print('4.) Lizard 🤏')
        print('5.) Spock 🖖')

        options_list = ['1','2','3','4','5']
        user_input1 = 0
        user_input2 = 0

        while user_input1 not in options_list:
            user_input1 = input(f'{self.players[0].name} Insert number here: ')
        self.players[0].pick_gesture(int(user_input1))

        if self.players[1].name == "Master Mind":
            user_input2 = random.randrange(1,5)

        else:   
            while user_input2 not in options_list:
                user_input2 = input(f'{self.players[1].name} Insert number here: ')

        self.players[1].pick_gesture(int(user_input2))
        self.compare_gesture(self.players[0].current_pick, self.players[1].current_pick)
        

    def choose_game_mode(self):
        options_list = ['singleplayer','multiplayer']
        user_input = ''
        while user_input not in options_list:
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
            print(f'{self.players[1].name} has won this round with {self.gesture_list[p2_pick].name}!\n')
            self.players[1].score += 1
        elif winner == 0:
            print(f'Both players chose {self.gesture_list[p2_pick].name}! This round is a Tie!\n')
        elif winner == 1:
            print(f'{self.players[0].name} has won this round with {self.gesture_list[p1_pick].name}!\n')
            self.players[0].score += 1        

    def display_winner(self):
        if self.players[0].score == 2:
            print(f'🎆 {self.players[0].name} wins! 🎆') 

        elif self.players[1].score == 2:
            print(f'🎆 {self.players[1].name} wins! 🎆')    

    def run_game(self):
        self.welcome_message()
        self.choose_game_mode()
        while self.players[0].score < 2 and self.players[1].score < 2:
            self.play_round()
        self.display_winner()
  