from Classes.dice import Dice
from Classes.stone import Stone
from Classes.spike import Spike
from Core.colors import Colors
from typing import List

class Backgammon:
    def __init__(self):
        self._moves = []
        self._dices = [Dice(), Dice()]
        self._spikes = [ Spike() for _ in range(24)]
        self._turn = None

    # setup default state of the game
    def _setup(self):
        black = [2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0]
        white = [0,0,0,0,0,5,0,3,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,2]
        for index in range(len(self._spikes)):
            for bIndex in range(black[index]):
                stone = Stone(self._spikes[index], color=Colors.Black)
                if self._spikes[index].isEmpty():
                    self._spikes[index].steal(stone, Colors.Black)
                else:
                    self._spikes[index].push(stone)
            for wIndex in range(white[index]):
                stone = Stone(self._spikes[index], color=Colors.White)
                if self._spikes[index].isEmpty():
                    self._spikes[index].steal(stone, Colors.White)
                else:
                    self._spikes[index].push(stone)
        
    # function that determins how's gonna play first   
    def _foreplay(self):
        self.diceRoll()
        while len(self._moves) > 2:
            self.diceRoll()
        if self._moves[0] > self._moves[1]:
            self._turn = Colors.Black
        else:
            self._turn = Colors.White

    # Dice roll with quad roll
    def diceRoll(self) -> None:
        total = []
        rolls = []
        for dice in self._dices:
            rolls.append(dice.throw())
        if rolls[-1] == rolls[0]:
            for _ in range(4):
                total.append(rolls[-1])
        else:
            for roll in rolls:
                total.append(roll) 
        self._moves = total

    # --------------------- COMMING SOON
    def getPossibleMoves(self) -> List:
        moves = []
        if self._turn:
            for index in range(len(self._spikes)-1,-1,-1):
                if self._spikes[index].color == Colors.White:
                    pass
        else:
            for index in range(len(self._spikes)):
                if self._spikes[index].color == Colors.Black:
                    pass

        return moves

    # main function for testing (MAYBE NEEDED?!)
    def main(self):
        self._setup()
        self._foreplay()
        print(self.getPossibleMoves())

    
    @property
    def board(self) -> List:
        return self._spikes

    @property
    def moves(self) -> List:
        return self._moves