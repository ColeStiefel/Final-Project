import pygame, sys, time, random
from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):

    def __init__(self,x,y,length,width,side_moves,direction):

        super().__init__()
        self.side_moves1 = side_moves
        self.side_moves2 = side_moves
        self.direction = direction
        self.rect = pygame.Rect(x,y,length,width)

    def move_left(self):
        self.rect.x -= 5
        self.side_moves1 -= 1
        if self.side_moves1 == 0:
            self.direction = 'right'
            self.side_moves1 = self.side_moves2 * 2

    def move_right(self):
        self.rect.x += 5
        self.side_moves1 -= 1
        if self.side_moves1 == 0:
            self.direction = 'left'
            self.side_moves1 = self.side_moves2 * 2
