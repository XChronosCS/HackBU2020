import pygame
from pygame.locals import *
import SFShotSetup, SFConstants
from SFConstants import *
from SFShotSetup import *
import sys
import os

class Square(pygame.sprite.Sprite):
    def __int__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'square_sprite.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.projectile = Projectile(SS_SPEED, SS_IMAGE, SS_DAMAGE, SS_PHANTOM)
        self.movement_speed = 5
        self.health = HEALTH




