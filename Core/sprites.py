import pygame, os
from Core.colors import Colors

assetsPath = f"{os.getcwd()}/Assets/Images/"

class Spike(pygame.sprite.Sprite):
    def __init__(self, color, position:tuple(),angle:int):
        super().__init__()
        self.image = pygame.transform.rotate(surface= pygame.image.load(f"{assetsPath}dark-spike.png") if color == Colors.Black else pygame.image.load(f"{assetsPath}light-spike.png"), angle=angle)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

class Stone(pygame.sprite.Sprite):
    def __init__(self, color, position:tuple()):
        super().__init__()
        self.image = pygame.image.load(f"{assetsPath}stone-p1.png") if color == Colors.Black else pygame.image.load(f"{assetsPath}stone-p2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = position