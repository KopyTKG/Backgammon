from Classes.dice import Dice
from Classes.stone import Stone
from typing import List

class Backgammon:
    def __init__(self):
        self._dices = [Dice(), Dice()]
        pass

    # Dice roll with quad roll
    def diceRoll(self) -> List:
        total = []
        rolls = []
        for dice in self._dices:
            rolls.append(dice.throw())
        if rolls[-1] == rolls[0]:
            for _ in range(4):
                total.append(rolls[-1])
        else:
            for roll in rolls:
                total.append(roll) 
        return total