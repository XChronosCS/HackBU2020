import pygame
from pygame.locals import *
import sys
import os


class Projectile(pygame.sprite.Sprite):
    def __init__(self,  shot_speed, shot_image, shot_damage, shot_phantom):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', shot_image)).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.speed = shot_speed
        self.damage = shot_damage
        self.phantom = shot_phantom

    def damage_deal(self):
        return self.damage
