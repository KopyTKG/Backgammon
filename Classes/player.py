from typing import List
from Core.colors import Colors
from Classes.spike import Spike
class Player:
    def __init__(self,color:Colors, spikes=[]):
        self._spikes = spikes
        self._color = color
        self._possibleMoves = []

    def addSpike(self, spike:tuple()) -> None:
        self._spikes.append(spike)
    
    def move(self, moveFrom:Spike, moveTo:Spike) -> None:
        if len(moveFrom[1].stones) > 1:
            stone = moveFrom[1].stones.pop()
            moveTo[1].stone.push(stone)
            self.addSpike(moveTo)
        else:
            stone = moveFrom[1].stones.pop()
            self._spikes.remove(moveFrom)
            moveTo[1].stone.push(stone)
            self.addSpike(moveTo)


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