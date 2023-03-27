from Core.stack import Stack
from Classes.stone import Stone
from typing import List

class Spike:
    def __init__(self, stones=Stack(), color=None): 
        self._stones = stones
        self._color = color
    
    def steal(self, stone, color) -> Stone:
        if not self.stones.isEmpty():
            tmp = self._stones.pop()
        self._stones = [stone]
        self._color = color
    
    def push(self, stone) -> None:
        self._stones.append(stone)

    def pop(self) -> Stone:
        return self._stones.pop()
    
    def isStealable(self) -> bool:
        return len(self._stones) < 2

    def isEmpty(self) -> bool:
        return not self._stones
    
    def __len__(self) -> int:
        return len(self._stones)
    
    @property
    def stones(self) -> List:
        return self._stones
        
    @property
    def color(self) -> str:
        return self._color