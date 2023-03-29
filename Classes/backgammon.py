from Classes.dice import Dice
from Classes.stone import Stone
from Classes.spike import Spike
from Classes.human import Human
from Classes.bar import Bar
from Classes.AI import Bot
from Core.colors import Colors
from typing import List

class Backgammon:
    def __init__(self):
        self._moves = []
        self._dices = [Dice(), Dice()]
        self._players = [Human(Colors.White), Human(Colors.Black)]
        self.bar = Bar(self._players)
        self._spikes = self.bar.setup()
        self._turn = None
        
    # function that determins how's gonna play first   
    def _foreplay(self):
        self.diceRoll()
        while len(self._moves) > 2:
            self.diceRoll()
        if self._moves[0] > self._moves[1]:
            self._turn = self._players[0]
        else:
            self._turn = self._players[1]

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
        self._turn = Colors.White if self._turn == Colors.Black else Colors.Black

    def _getPossibleMoves(self) -> None:
        playerSpikes = self._turn.spikes
        moves = []
        if self._turn == self._players[1]:
            total = 0
            for move in self._moves:
                total += move
                for spike in playerSpikes:
                    spikeTo = spike - move
                    if spikeTo > -1 and self._spikes[spikeTo].isStealable():
                        moves.append((spike ,spikeTo))
                
            for spike in playerSpikes:
                spikeTo = spike - total
                if spikeTo > -1 and self._spikes[spikeTo].isStealable():
                    moves.append((spike ,spikeTo))
        else:
            total = 0
            for move in self._moves:
                total += move
                for spike in playerSpikes:
                    spikeTo = spike + move
                    if spikeTo < len(self._spikes) and self._spikes[spikeTo].isStealable():
                        moves.append((spike ,spikeTo))
                    
            for spike in playerSpikes:
                spikeTo = spike + total
                if spikeTo < len(self._spikes) and self._spikes[spikeTo].isStealable():
                    moves.append((spike ,spikeTo))

        self._turn.possibleMoves = moves

    # main function for testing (MAYBE NEEDED?!)
    def main(self):
        #self._setup()
        self._foreplay()
        self._getPossibleMoves()
        self._turn.getMove()

    
    @property
    def board(self) -> List:
        return self._spikes

    @property
    def moves(self) -> List:
        return self._moves