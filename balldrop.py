import pygame, sys, time, random
from pygame.locals import *
from ball import ball
from hoop import hoop

pygame.init()

WHITE = (255,255,255)
DISPLAYSURF = pygame.display.set_mode((300,400), 0, 32)
FPS = 10
fpsClock = pygame.time.Clock()

HOOP = pygame.image.load('Basketball Hoop.png')
HOOP = pygame.transform.scale(HOOP, (45,45))

pygame.display.set_caption("Ball Drop")

ballob = ball(135,0)
hoopob = hoop(0)

direction = 'right'

opener = 'true'

def opening_screen():
    BASICFONT_large = pygame.font.Font('freesansbold.ttf', 60)
    txt = BASICFONT_large.render('Ball Dropper',1,WHITE)
    ball_dropper_rect = DISPLAYSURF.get_rect()
    ball_dropper_rect.center = (212,250)
    DISPLAYSURF.blit(txt, ball_dropper_rect)

def switch_opener(opener):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #use pygame.mouse.get_pos

def hoop_move():
    if direction == 'right':
        hoopob.move_right()
    if direction == 'left':
        hoopob.move_left()

def switch_direction(direction):
    if direction == 'right' and hoopob.return_x() == 255:
        direction = 'left'
    if direction == 'left' and hoopob.return_x() == 0:
        direction = 'right'
    return direction

def update_hoop():
    DISPLAYSURF.blit(HOOP, (hoopob.rect.x,355,45,45))

while True:
    DISPLAYSURF.fill(WHITE)

    if opener() == 'true'
        opening_screen()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    hoop_move()
    update_hoop()

    direction = switch_direction(direction)

    pygame.display.update()
    fpsClock.tick(FPS)
