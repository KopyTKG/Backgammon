from typing import List
from Core.colors import Colors
from Classes.spike import Spike
class Player:
    def __init__(self,color:Colors):
        self._spikes = []
        self._board = []
        self._color = color
        self._possibleMoves = []
        self._opositePlayer = None

    def addSpike(self, spike:int) -> None:
        self._spikes.append(spike)
    
    def move(self, moveFrom:Spike, moveTo:Spike) -> None:
        steal = self._opositePlayer.color
        stone = stolen = None

        # get moving stone (remove spike if empty)
        if len(self._board[moveFrom].stones) > 1:
            stone = self._board[moveFrom].stones.pop()
        else:
            stone = self._board[moveFrom].stones.pop()
            self._spikes.remove(moveFrom)

        # move stone
        if self._board[moveTo].color != self._color:
            stolen = self._board[moveTo].steal(stone, self._color)
        else:
            self._board[moveTo].push(stone)

        return [self._opositePlayer, stolen]

    def setOpositPlayer(self, player) -> None:
        self._opositePlayer = player

    def setBoard(self, board) -> None:
        self._board = board

    @property
    def spikes(self) -> List:
        return self._spikes
    
    @property
    def color(self) -> Colors:
        return self._color

    @property
    def possibleMoves(self) -> List:
        return self._possibleMoves

    @possibleMoves.setter
    def possibleMoves(self, moves:List) -> None:
        self._possibleMoves = moves