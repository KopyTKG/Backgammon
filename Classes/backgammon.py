from Classes.dice import Dice
from Classes.stone import Stone
from Classes.spike import Spike
from Classes.human import Human
from Classes.AI import Bot
from Core.colors import Colors
from typing import List

class Backgammon:
    def __init__(self):
        self._moves = []
        self._dices = [Dice(), Dice()]
        self._spikes = []
        for index in range(24):
            self._spikes.append(Spike())
        self._players = [Human(Colors.White), Human(Colors.Black)]
        self._turn = None

    # setup default state of the game
    def _setup(self):
        black = [2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0]
        white = [0,0,0,0,0,5,0,3,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,2]
        for index in range(len(self._spikes)):
            if black[index] > white[index]:
                self._players[0].addSpike((index, self._spikes[index]))
            elif black[index] < white[index]:
                self._players[1].addSpike((index, self._spikes[index]))

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
                    spikeTo = spike[0] - move
                    if spikeTo > -1 and self._spikes[spikeTo].isStealable():
                        moves.append((spike[1] ,self._spikes[spikeTo]))
                
            for spike in playerSpikes:
                spikeTo = spike[0] - total
                if spikeTo > -1 and self._spikes[spikeTo].isStealable():
                    moves.append((spike[1] ,self._spikes[spikeTo]))
        else:
            total = 0
            for move in self._moves:
                total += move
                for spike in playerSpikes:
                    spikeTo = spike[0] + move
                    if spikeTo < len(self._spikes) and self._spikes[spikeTo].isStealable():
                        moves.append((spike[1] ,self._spikes[spikeTo]))
                    
            for spike in playerSpikes:
                spikeTo = spike[0] + total
                if spikeTo < len(self._spikes) and self._spikes[spikeTo].isStealable():
                    moves.append((spike[1] ,self._spikes[spikeTo]))

        self._turn.possibleMoves = moves

    # main function for testing (MAYBE NEEDED?!)
    def main(self):
        self._setup()
        self._foreplay()
        self._getPossibleMoves()
        self._turn.getMove()

    
    @property
    def board(self) -> List:
        return self._spikes

    @property
    def moves(self) -> List:
        return self._moves