from random import choice

class Dice():
    def __init__(self, sides=6):
        self.__sides = [x for x in range(1,sides+1)]

    def throw(self) -> int:
        return choice(self.__sides)