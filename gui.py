from Classes.backgammon import Backgammon
from Core.ui import FPS
from Core.colors import Colors
from Core.sprites import Stone, Spike
import sys, pygame, os, yaml

class UI():
    def __init__(self):
        pygame.init()
        
        self._modes = {"fullscreen": (pygame.HWSURFACE | pygame.FULLSCREEN), "bordless": pygame.NOFRAME}
        with open(f"{os.getcwd()}/Configs/master.yml", "r") as opened:
            self._config = yaml.safe_load(opened)

        self.backgammon = Backgammon()
        self.backgammon.main()
        self._board = []
        self._bg = self._config["background"][0], self._config["background"][1], self._config["background"][2]
        self._flags = self._modes["bordless"]
        self._res = (self._config["resolution"][0],self._config["resolution"][1])
        self._color = (125,175,0)
        self._border = {"x": 20, "y":20}
        self._screen = pygame.display.set_mode(self._res, flags=self._flags, vsync=0)
        self._screen.fill(self._bg)
        self._currentRoll = []
        self._assetsPath = f"{os.getcwd()}/Assets/Images/"
        self._field = pygame.image.load(f"{self._assetsPath}field.png")
        self._fieldSize = (self._field.get_width(), self._field.get_height())
        self._rolled = False
        self._mousePosition = (0,0)
        self._diceIMG = [pygame.image.load(f"{self._assetsPath}dice.png"),pygame.image.load(f"{self._assetsPath}dice-hvr.png")]
        self._playerIMG = [pygame.image.load(f"{self._assetsPath}PlayerTwo.png"),pygame.image.load(f"{self._assetsPath}PlayerOne.png")]
        self._diceSize = 100
        self._stoneSize, self._stoneTile = 75, 105
        self._splitter = 160
        self._font = pygame.font.SysFont(f"{os.getcwd()}/Assets/Fonts/NotoSans-Regular.ttf", 48)

        self._stoneSprites = pygame.sprite.Group()
        self._spikeSprites = pygame.sprite.Group()

    # rendering for spikes
    def _spikes(self) -> None:
        # top 12 spikes
        x = (self._res[0] //2 + self._fieldSize[0] //2) - self._stoneTile
        y = (self._res[1] //2 - self._fieldSize[1] // 2)
        last = Colors.White
        for index in range(12):
            shiftX = 0
            if index % 6 == 0 and index != 0:
                shiftX = self._splitter
            x -= shiftX
            newSpike = Spike(last, (x,y), 0)
            self._spikeSprites.add(newSpike)
            last = Colors.White if last == Colors.Black else Colors.Black
            x -= self._stoneTile
        # bottom 12 spikes
        x += self._stoneTile
        y = (self._res[1] //2 + self._fieldSize[1] // 2) - 394
        for index in range(12, 24):
            shiftX = 0
            if index % 6 == 0 and index != 12:
                shiftX = self._splitter
            x += shiftX
            newSpike = Spike(last, (x,y),180)
            self._spikeSprites.add(newSpike)
            last = Colors.White if last == Colors.Black else Colors.Black
            x += self._stoneTile

    # rendering for stones
    def _stones(self) -> None:
        # starting position for rendering
        x = (self._res[0] //2 + self._fieldSize[0] //2) - ((self._stoneTile - self._stoneSize)//2 + self._stoneSize)
        y = self._res[1] //2 - self._fieldSize[1] // 2
        # Top 12 render
        for index in range(12):
            shiftX = 0
            if index % 6 == 0 and index != 0:
                shiftX = self._splitter
            current = self._board[index]
            x -= shiftX
            y = self._res[1] //2 - self._fieldSize[1] // 2
            for stone in range(len(current)):
                newStone = Stone(current.color, (x,y))
                self._stoneSprites.add(newStone)
                y += self._stoneSize
            x -= self._stoneTile
        x = (self._res[0] //2 - self._fieldSize[0] //2) + (self._stoneTile - self._stoneSize)//2
        
        # Bottom 12 render
        for index in range(12,24):
            shiftX = 0
            if index % 6 == 0 and index != 12:
                shiftX = self._splitter
            current = self._board[index]            
            x += shiftX
            y = (self._res[1] //2 + self._fieldSize[1] //2) - self._stoneSize
            for stone in range(len(current)):
                newStone = Stone(current.color, (x,y))
                self._stoneSprites.add(newStone)
                y -= self._stoneSize
            x += self._stoneTile

    # rendering for the board
    def _boardRnd(self) -> None:
        border = 60
        scale = .75
        y = border
        for player in self._playerIMG:
            self._screen.blit(
                pygame.transform.scale(player, 
                        (
                            player.get_width() * scale, 
                            player.get_height() * scale
                        )
                    ),
                (
                    25,
                    y
                )
            )
            y =  border if y != border else self._res[1] - (border + player.get_height() * scale)
        self._screen.blit(
            self._field,
            (
                self._res[0]//2 - (self._fieldSize[0] // 2),
                self._res[1]//2 - (self._fieldSize[1] // 2)
            )
        )


    # rendering for dice rolled numbers
    def _rolls(self) -> None:
        if len(self._currentRoll) > 0:
            lenght = len(self._currentRoll) / 2
            position = 0
            if lenght >= 2:
                indent = [(self._res[0]//2)+x for x in [-150,-50,50,150]]
            else:
                indent = [(self._res[0]//2)+x for x in [-50,50]]

            for roll in self._currentRoll:
                self._screen.blit(
                    self._font.render(str(roll), True, self._color)
                    ,(indent[position], self._border["x"]))
                position +=1

    # rendering for dices / hover function
    def _dice(self, dice):
        self._screen.blit(dice, (self._res[0] - self._diceSize-self._border["x"], self._border["y"]))

    def GUIrender(self) -> None:
        self._boardRnd()
        self._rolls()

    def Setup(self) -> None:
        self._spikes()
        self._stones()
    
    def run(self):
        fps = FPS((0,0,255))
        self._board = self.backgammon.board
        self.Setup()

        while True:
            # close event
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            self._screen.fill(self._bg)
            
            # get board state
            self._board = self.backgammon.board
            # GUI rendering
            self.GUIrender()

            self._spikeSprites.draw(self._screen)
            self._stoneSprites.draw(self._screen)
            
            # FPS Counter
            fps.clock.tick(144)
            fps.render(self._screen)

            # mouse tracking
            self._mousePosition = pygame.mouse.get_pos()
            
            
            # Dice render and Dice hover
            if self._mousePosition[0] > self._res[0] - self._diceSize - self._border["x"] and self._mousePosition[0] < self._res[0] - self._border["y"]:
                if self._mousePosition[1] > self._border["x"] and self._mousePosition[1] < self._border["y"] + self._diceSize:
                    self._dice(self._diceIMG[1])
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if pygame.mouse.get_pressed()[0] and not self._rolled:
                        self.backgammon.diceRoll()
                        self._currentRoll = self.backgammon.moves
                        self._rolled = True
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self._dice(self._diceIMG[0])
                    self._rolled = False

            else: 
                self._rolled = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self._dice(self._diceIMG[0])
            
            pygame.display.update()
            



ui = UI()
if __name__ == "__main__":
    ui.run()