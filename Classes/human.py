from Classes.player import Player

class Human(Player):
    def __init__(self, color):
        super().__init__(color=color)

    def getMove(self) -> Player:
        index = 1
        for move in self.possibleMoves:
            print(f"{index}) {move}")
            index += 1
        try:
            choice = int(input("Choose move: "))
        except:
            choice = 1
        choice -= 1
        return self.move(self.possibleMoves[choice][0], self.possibleMoves[choice][1])