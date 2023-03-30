from Classes.stone import Stone
from Core.stack import Stack
from Core.colors import Colors
from typing import List

class Spike:
    def __init__(self, color=None): 
        self._stones = Stack()
        self._color = color
    
    def steal(self, stone, color) -> Stone:
        stone = None
        if len(self.stones) > 0:
            stone = self._stones.pop()
        self._stones.push(stone)
        self._color = color
        return stone
    
    def push(self, stone) -> None:
        self._stones.push(stone)

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
    
    @color.setter
    def color(self, color:Colors) -> None:
        self._color = color