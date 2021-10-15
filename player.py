class Player:
    def __init__(self):
        self.score = 0
        self.current_pick = None

    def pick_gesture(self, pick):
        self.current_pick = (pick - 1)