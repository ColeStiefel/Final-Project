#necessary
import pygame, sys, time, random
from pygame.locals import *

#creating the 'Ball' class
class Ball(pygame.sprite.Sprite):

    #making the sprite
    def __init__(self,x,y):

        super().__init__()

        #giving it the starting x and y coordinate and making its rectangle
        self.x = x
        self.y = y
        #if I did this again I would make the ball's rectangle the right size, but like the hoop, I made it only the bottom line
        #my intention was to ensure that it would not count as winning if the side of the ball hit the side of the hoop, after a miss
        self.rect = pygame.Rect(self.x,self.y,30,1)

    #moving the ball down
    def move_down(self):
        self.rect.y += 5

    #moving the ball left it is not at the edge of the screen
    def move_left(self):
        if self.rect.x != 5:
            self.rect.x -= 10

    #moving hte ball right if it not at the edge of the screen
    def move_right(self):
        if self.rect.x != 265:
            self.rect.x += 10

    #reseting the ball at the top and center of the screen
    def reset(self):
        self.rect.x = 135
        self.rect.y = 30
