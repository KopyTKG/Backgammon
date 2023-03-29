from Classes.player import Player

class Human(Player):
    def __init__(self, color):
        super().__init__(color=color)

    def getMove(self):
        for move in self.possibleMoves:
            print(move)