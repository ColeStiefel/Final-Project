import pygame, sys, time, random
from pygame.locals import *

class Ball(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,30,1)

    def move_down(self):
        self.rect.y += 5

    def move_left(self):
        if self.rect.x != 0:
            self.rect.x -= 5

    def move_right(self):
        if self.rect.x != 270:
            self.rect.x += 5

    def reset(self):
        self.rect.x = 135
        self.rect.y = 30
