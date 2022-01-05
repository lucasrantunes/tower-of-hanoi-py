from stack import Stack
class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.stacks = [Stack(difficulty), Stack(), Stack()]