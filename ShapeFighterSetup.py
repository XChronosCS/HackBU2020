import os
import pygame
from pygame import *
from pygame.locals import *
import sys
from PythonLifeHacks import *
"""
import SFGameGui, SFCharacters, SFConstants
from SFGameGui import *
from SFConstants import *
from SFCharacters import *
"""

screenSize(800, 400)
setBackgroundImage(os.path.join('images', 'stage_background.png'))
square = makeSprite('images/square_sprite.png')
square_x = 200
square_y = 200
moveSprite(square, square_x, square_y)
showSprite(square)

main = True
while main:
    """
    Need to figure out how to program to allow for exit using the red X button.
    if pygame.mouse.get_pressed():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("This works")
                main = False
    """
    if keyPressed("esc"):
            main = False
    if keyPressed("right"):
        if square_x < 750:
            square_x += 1
            moveSprite(square, square_x, square_y)
    if keyPressed("left") and 50 < square_x:
        square_x -= 1
        moveSprite(square, square_x, square_y)
    if keyPressed("down"):
        if square_y < 390:
            square_y += 1
            moveSprite(square, square_x, square_y)
    if keyPressed("up"):
        if 10 < square_y:
            square_y -= 1
            moveSprite(square, square_x, square_y)

pygame.quit()
sys.exit()