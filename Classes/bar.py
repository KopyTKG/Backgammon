from Classes.stone import Stone
from Classes.spike import Spike
from Core.colors import Colors
from typing import List

class Bar:
    def __init__(self, players, pOne=[0,0,0,0,0,5,0,3,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,2], pTwo=[2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0]):
        self._playerOne = pOne
        self._playerTwo =  pTwo
        self._players = players
    
    def setup(self) -> List:
        board = []
        for i in range(24):
            color = None
            newSpike = Spike()
            count = 0
            if self._playerOne[i] > self._playerTwo[i]:
                color = Colors.White
                count = self._playerOne[i]
                self._players[0].addSpike(i)

            elif self._playerOne[i] < self._playerTwo[i]:
                color = Colors.Black
                count = self._playerTwo[i]
                self._players[1].addSpike(i)

            for _ in range(count):
                stone = Stone(currentLocation=newSpike, color=color)
                if newSpike.isEmpty():
                    newSpike.steal(stone, color)
                else:
                    newSpike.push(stone)

            board.append(newSpike)
        return board