from Classes.stone import Stone
from typing import List

class Spike:
    def __init__(self, stones=False, color=None): 
        self._stones = []
        self._color = color
    
    def steal(self, stone, color) -> Stone:
        if len(self.stones) > 0:
            tmp = self._stones.pop(-1)
        self._stones.append(stone)
        self._color = color
    
    def push(self, stone) -> None:
        self._stones.append(stone)

    def pop(self) -> Stone:
        return self._stones.pop(-1)
    
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