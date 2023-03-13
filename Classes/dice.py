from random import choice

class Dice():
    def __init__(self, sides=[1,2,3,4,5,6]):
        self.__sides = sides

    def throw(self) -> int:
        return choice(self.__sides)