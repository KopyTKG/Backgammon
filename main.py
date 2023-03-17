from Classes.dice import Dice
from Classes.stone import Stone
from Core.ui import FPS
import sys, pygame, os
 
class Backgammon():
    def __init__(self):
        pygame.init()
        self._bg = 255,255,255
        self._flags = pygame.HWSURFACE # | pygame.NOFRAME # | pygame.FULLSCREEN 
        self._res = (1920,1080)
        self._color = (125,175,0)
        self._screen = pygame.display.set_mode(self._res, flags=self._flags, vsync=0)
        self._screen.fill(self._bg)
        self._dices = [Dice(), Dice()]
        self._currentRoll = []
        self._assetsPath = f"{os.getcwd()}/Assets/Images/"
        self._field = pygame.image.load(f"{self._assetsPath}field.png")
        self._fieldSize = (self._field.get_width(), self._field.get_height())
        self._rolled = False
        self._mousePosition = (0,0)
        self._diceIMG = [pygame.image.load(f"{self._assetsPath}dice.png"),pygame.image.load(f"{self._assetsPath}dice-hvr.png")]
        self._stoneIMG = [pygame.image.load(f"{self._assetsPath}stone-p1.png"),pygame.image.load(f"{self._assetsPath}stone-p2.png")]
        self._diceSize = 100
        self._font = pygame.font.SysFont(f"{os.getcwd()}/Assets/Fonts/NotoSans-Regular.ttf", 48)

    def _diceRoll(self) -> None:
        self._currentRoll = []
        for dice in self._dices:
            self._currentRoll.append(dice.throw())

    def _render(self):
        if len(self._currentRoll) > 0:
            indent = -30
            for roll in self._currentRoll:
                self._screen.blit(
                    self._font.render(str(roll), True, self._color)
                    ,(self._res[0] // 2 + indent, 20))
                indent *= -1
        
        self._screen.blit(
            self._field,
            (self._res[0]//2 - (self._fieldSize[0] //2), self._res[1]//2 - (self._fieldSize[1] // 2))
        )

    def _renderDice(self, dice):
        self._screen.blit(dice, (self._res[0] - self._diceSize-20,20))

    def run(self):
        fps = FPS((0,0,255))
        while True:
            self._screen.fill(self._bg)
            # FPS Counter
            fps.clock.tick(144)
            fps.render(self._screen)
            self._mousePosition = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

            self._render()

            for y in range(-400, 480, 80):
                if y != 0: 
                    for x in range(-630,0, 105):
                        self._screen.blit(self._stoneIMG[1], (self._res[0] // 2 + x - 37.5 ,self._res[1]//2 + y - 37.5))
                    for x in range(100, 730, 105):
                        self._screen.blit(self._stoneIMG[0], (self._res[0] // 2 + x - 37.5 ,self._res[1]//2 + y - 37.5))


            if self._mousePosition[0] > self._res[0] - self._diceSize - 20 and self._mousePosition[0] < self._res[0] - 20:
                if self._mousePosition[1] > 20 and self._mousePosition[1] < 20 + self._diceSize:
                    self._renderDice(self._diceIMG[1])
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if pygame.mouse.get_pressed()[0] and not self._rolled:
                        self._diceRoll()
                        self._rolled = True
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self._renderDice(self._diceIMG[0])
                    self._rolled = False

            else: 
                self._rolled = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self._renderDice(self._diceIMG[0])
            
            pygame.display.update()
            



BK = Backgammon()
if __name__ == "__main__":
    BK.run()