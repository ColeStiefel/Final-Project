import pygame, sys, time, random
from pygame.locals import *

class Hoop(pygame.sprite.Sprite):

    def __init__(self,x):

        super().__init__()
        self.x = x
        self.rect = pygame.Rect(self.x,355,45,1)

    def return_x(self):
        return self.rect.x

    def move_right(self):
        self.rect.x += 5

    def move_left(self):
        self.rect.x -= 5

    def reset(self):
      self.rect.x = 0
