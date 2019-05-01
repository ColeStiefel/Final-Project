import pygame, sys, time, random
from pygame.locals import *

hoop = pygame.image.load('Basketball Hoop.png')
hoop = pygame.transform.scale(hoop, (35,35))

class hoop(pygame.sprite.Sprite):

    def __init__(self,x):

        super().__init__()
        self.x = x
        self.rect = pygame.Rect(self.x,365,35,1)

    def return_x(self):
        return self.x

    def move_right(self):
        self.rect.x += 5

    def move_left(self):
        self.rect.y += 5
