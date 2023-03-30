from Classes.dice import Dice
from Classes.stone import Stone
from Classes.spike import Spike
from Classes.human import Human
from Classes.bar import Bar
from Classes.AI import Bot
from Core.colors import Colors
from typing import List
import subprocess

class Backgammon:
    def __init__(self):
        # store for dice rolls
        self._moves = []
        self._dices = [Dice(), Dice()]
        self._players = [
            Human(color=Colors.White), 
            Human(color=Colors.Black)
        ]
        self.bar = Bar(self._players)
        self._spikes = self.bar.setup()
        self._stolen = []
        self._turn = None
        # link board to players for move function
        for player in self._players:
            player.setBoard(self._spikes)
        # setting oposite player
        self._players[0].setOpositPlayer(self._players[-1])
        self._players[-1].setOpositPlayer(self._players[0])
        
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

    # Function takes playes spikes and current moves to determin next play
    def _getPossibleMoves(self, move) -> None:
        playerSpikes = self._turn.spikes
        moves = []
        if self._turn == self._players[1]:
            for spike in playerSpikes:
                spikeTo = spike - move
                if spikeTo > -1 and self._spikes[spikeTo].isStealable():
                    moves.append((spike ,spikeTo))
                
        else:
            for spike in playerSpikes:
                spikeTo = spike + move
                if spikeTo < len(self._spikes) and self._spikes[spikeTo].isStealable():
                    moves.append((spike ,spikeTo))

        self._turn.possibleMoves = moves

    # tmp function for shell rendering
    def RenderBoard(self, board):
        for index in range(len(board)//2):
            left = index
            right = (len(board)-1)-index
            print(f"C:{board[left].color} - {len(board[left].stones)} | C:{board[right].color} - {len(board[right].stones)} ")

    # Main game cycle
    def main(self):
        self._foreplay()
        for _ in range(5):
            output = []
            display = self._moves.copy()
            for move in self._moves:
                subprocess.run("clear")
                self._getPossibleMoves(move)
                self.RenderBoard(self._spikes)
                print(f"Current player: {self._turn.color}")
                print(f"Rolled: {display}")
                output = self._turn.getMove()
                if output[1] != None:
                    self._stolen.append(output[1])
                print(self._stolen)
                display.pop(0)
            self._turn = output[0]
            self.diceRoll() 

    
# Properties for GUI
    @property
    def board(self) -> List:
        return self._spikes
    @property
    def moves(self) -> List:
        return self._moves