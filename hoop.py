#necessary
import pygame, sys, time, random
from pygame.locals import *

#creating the 'Hoop' class
class Hoop(pygame.sprite.Sprite):

    #making the hoop sprite
    def __init__(self,x):

        super().__init__()

        #the x coordinate and making it's rectangle
        #note the rectangle is only the top line of the hoop so it does not count as hitting the ball and winning
        self.x = x
        self.rect = pygame.Rect(self.x,355,45,1)

    #return the hoop's x value
    def return_x(self):
        return self.rect.x

    #move the hoop to the right
    def move_right(self):
        self.rect.x += 5

    #move the hoop left
    def move_left(self):
        self.rect.x -= 5

    #reset the hoop, but randomize the starting position some so that rounds are not always the same
    def reset(self):
      random_hoop_spawn = random.randint(1,40)
      self.rect.x = random_hoop_spawn * 5
