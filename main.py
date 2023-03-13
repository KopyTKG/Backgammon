from Classes.dice import Dice
from Classes.stone import Stone
def main():
    fDice = Dice()
    s = Stone(0)
    for _ in range(20):
        s.location = fDice.throw()
        print(s.location())
    
    print(s.locations)


if __name__ == "__main__":
    main()