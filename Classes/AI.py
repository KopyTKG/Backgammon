from Classes.player import Player

class Bot(Player):
    def __init__(self, color, spikes=[]):
        super().__init__(color=color, spikes=spikes)

    def getMove(self):
        pass