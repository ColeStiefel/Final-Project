#necessary
import pygame, sys, time, random
from pygame.locals import *

#making class 'Obastacle'
class Obstacle(pygame.sprite.Sprite):

    #making sprite with given parameters
    def __init__(self,x,y,length,width,side_moves,direction):

        #necessary
        super().__init__()

        #side_moves1 keeps track of how many times the obstacle has already moved
        self.side_moves1 = side_moves
        #side_moves2 does not change and remembers how many times it should move back and forth
        #side_moves1 and 2 allow for the obstacle to move to each side the right amount of times and then turn the other way
        self.side_moves2 = side_moves
        #randomly gives the obstacle a direction so levels are not the same every time
        if direction == 'either':
            random_direction = random.randint(1,2)
            if random_direction == 1:
                self.direction = 'left'
            if random_direction == 2:
                self.direction = 'right'
        #or if the obstacle is supposed to go a certain way it can be told to go left or right
        if direction == 'left':
            self.direction = 'left'
        if direction == 'right':
            self.direction = 'right'
        #the obstacle's rectangle
        self.rect = pygame.Rect(x,y,length,width)

    #moves it left unless it has already moved left as much as it is supposed to, in which case it changes direction and resets the side_moves1
    def move_left(self):
        self.rect.x -= 5
        self.side_moves1 -= 1
        if self.side_moves1 == 0:
            self.direction = 'right'
            self.side_moves1 = self.side_moves2 * 2

    #same ass move_left but going right
    def move_right(self):
        self.rect.x += 5
        self.side_moves1 -= 1
        if self.side_moves1 == 0:
            self.direction = 'left'
            self.side_moves1 = self.side_moves2 * 2
