from Core.stack import Stack
from Classes.stone import Stone

class Spike:
    def __init__(self, stones=[], color=None): 
        self._stones = Stack(stones)
        self._color = color
    
    def steal(self, stone, color) -> Stone:
        tmp = self._stones.pop()
        self._stones = [stone]
        self._color = color
    
    def add(self, stone) -> None:
        self._stones.append(stone)

    def pop(self) -> Stone:
        return self._stones.pop()

    @property
    def stones(self) -> List:
        return self.__stones
