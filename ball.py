import pygame, sys, time, random
from pygame.locals import *

ball = pygame.image.load('Basketball.png')
ball = pygame.transform.scale(ball, (30,30))

class ball(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x+30,self.y,30,1)
