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
square_x = 400
square_y = 200
moveSprite(square, square_x, square_y)
showSprite(square)
enemy_square = makeSprite('images/enemy_square.png')
moveSprite(enemy_square, 200, 200)
showSprite(enemy_square)
player_projectiles = []

class Projectile(pygame.sprite.Sprite):
    def __init__(self, shot_x, shot_y, shot_speed, shot_image, shot_damage, shot_phantom):
        self.sprite = makeSprite((os.path.join('images', shot_image)))
        self.x = shot_x
        self.y = shot_y
        self.speed = shot_speed
        self.damage = shot_damage
        self.phantom = shot_phantom



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
    if keyPressed("space"):
        player_projectiles.append(Projectile(square_x, square_y, 5, 'player_missile.png', 5, False))


    '''
    if touching(square, enemy_square):
        hideSprite(enemy_square)
    if not touching(square, enemy_square):
        unhideAll()
    '''



pygame.quit()
sys.exit()