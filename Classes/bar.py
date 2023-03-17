from Core.stack import Stack
from Classes.stone import Stone

class Bar:
    def __init__(self):
        self._playerOneBar = Stack()
        self._playerTwoBar = Stack()
    
    def add(self, stone, player) -> None:
        if player == "One":
            self._playerOneBar.push(stone)
        elif player == "Two":
            self._playerTwoBar.push(stone)
    
    def pop(self, player) -> Stone:
        if player == "One":
            return self._playerOneBar.pop()
        elif player == "Two":
            return self._playerTwoBar.pop()