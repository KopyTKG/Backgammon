from Classes.player import Player

class Human(Player):
    def __init__(self, color, spikes=[]):
        super().__init__(color=color, spikes=spikes)

    def getMove(self):
        for move in self.possibleMoves:
            print(move)