import pygame, sys, time, random
from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):

    def __init__(self,x,y,length,width):

        super().__init__()
        self.rect = pygame.Rect(x,y,length,width)
