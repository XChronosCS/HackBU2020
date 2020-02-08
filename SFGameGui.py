import pygame
from pygame.locals import *
import sys
import os
import SFConstants as Const
from SFConstants import *


pygame.init()

class Layer:
    def __init__(self):
        self.game_screen = pygame.display.set_mode(SCREENSIZE)


class Window:
    def __init__(self, screen):
        self.Screen = screen

    def get_background(self, image):
        background = pygame.image.load(os.path.join('images', image)).convert()
        background_resize = pygame.transform.scale(background, SCREENSIZE)
        self.Screen.blit(background_resize, BASE_POS)







