import sys, pygame, os

class FPS:
    def __init__(self, color=(255,0,0)):
        self._color = color
        self.clock = pygame.time.Clock()
        self._font = pygame.font.SysFont(f"{os.getcwd()}/Assets/Fonts/NotoSans-Regular.ttf", 32)
        self._text = self._font.render(str(int(self.clock.get_fps())), True, self._color)
 
    def render(self, screen):
        self._text = self._font.render(str(int(self.clock.get_fps())), True, self._color, (255,255,255))
        screen.blit(self._text, (0, 0))