import pygame, sys, time, random
from pygame.locals import *
from ball import ball
from hoop import hoop

DISPLAYSURF = pygame.display.set_mode((300,400), 0, 32)
FPS = 10
fpsClock = pygame.time.Clock()

pygame.display.set_caption("Ball Drop")

ballob = ball(135,0)
hoopob = hoop(0)

direction = 'right'

def hoop_move():
    if direction == 'right'
        if hoopob.return_x() != 300:
            hoopob.move_right

    if direction == 'left'

def main():

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

main()
