import pygame
from pygame import *
"""
import SFGameGui, SFCharacters, SFConstants
from SFGameGui import *
from SFConstants import *
from SFCharacters import *
"""

pygame.init()

game_window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Shape Fighters")

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()