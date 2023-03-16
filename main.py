from Classes.dice import Dice
from Classes.stone import Stone
import sys, pygame, os

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self._font = pygame.font.SysFont(f"{os.getcwd()}/Assets/Fonts/NotoSans-Regular.ttf", 32)
        self._text = self._font.render(str(int(self.clock.get_fps())), True, (0,255,0))
 
    def render(self, screen):
        self._text = self._font.render(str(int(self.clock.get_fps())), True, (255,0,0),(255,255,255))
        screen.blit(self._text, (0, 0))
 
class Backgammon():
    def __init__(self):
        pygame.init()
        self._bg = 255,255,255
        self._flags = pygame.HWSURFACE | pygame.NOFRAME # | pygame.FULLSCREEN 
        self._res = (1920,1080)
        self._screen = pygame.display.set_mode(self._res, flags=self._flags, vsync=0)
        self._screen.fill(self._bg)
        self._dices = [Dice(), Dice()]
        self._currentRoll = []
        self._rolled = False
        self._mousePosition = (0,0)
        self._diceIMG = [pygame.image.load(f"{os.getcwd()}/Assets/Images/dice.png"),pygame.image.load(f"{os.getcwd()}/Assets/Images/dice-hvr.png")]
        self._diceSize = 100

    def _diceRoll(self) -> None:
        self._currentRoll = []
        for dice in self._dices:
            self._currentRoll.append(dice.throw())


    def _renderDice(self, dice):
        self._screen.blit(dice, (self._res[0] - self._diceSize-20,20))


    def run(self):
        fps = FPS()
        while True:
            self._screen.fill(self._bg)
            # FPS Counter
            fps.clock.tick(60)
            fps.render(self._screen)
            self._mousePosition = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

                if self._mousePosition[0] > self._res[0] - self._diceSize - 20 and self._mousePosition[0] < self._res[0] - 20:
                    if self._mousePosition[1] > 20 and self._mousePosition[1] < 20 + self._diceSize:
                        if pygame.mouse.get_pressed()[0] and not self._rolled:
                            self._diceRoll()
                            self._rolled = True
                            print(self._currentRoll)
                else:
                    self._rolled = False
            if self._mousePosition[0] > self._res[0] - self._diceSize - 20 and self._mousePosition[0] < self._res[0] - 20:
                if self._mousePosition[1] > 20 and self._mousePosition[1] < 20 + self._diceSize:
                    self._renderDice(self._diceIMG[1])
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self._renderDice(self._diceIMG[0])
            else: 
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self._renderDice(self._diceIMG[0])
            pygame.display.update()
            



BK = Backgammon()
if __name__ == "__main__":
    BK.run()