import pygame, sys, time, random
from pygame.locals import *
from ball import Ball
from hoop import Hoop

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
DISPLAYSURF = pygame.display.set_mode((300,400), 0, 32)
FPS = 10
fpsClock = pygame.time.Clock()

HOOP = pygame.image.load('Basketball Hoop.png')
HOOP = pygame.transform.scale(HOOP, (45,45))

BALL = pygame.image.load('Basketball.png')
BALL = pygame.transform.scale(BALL, (30,30))

pygame.display.set_caption("Ball Drop")

ballob = Ball(135,0)
hoopob = Hoop(0)

direction = 'right'

play_rect = DISPLAYSURF.get_rect()

opener = 'true'

def opening_screen():
    BASICFONT = pygame.font.Font('freesansbold.ttf', 40)
    txt_ball_dropper = BASICFONT.render('Ball Dropper',1,BLACK)
    txt_play = BASICFONT.render('Play',1,BLACK)
    ball_dropper_rect = DISPLAYSURF.get_rect()
    #play_rect would be defined here but it is used in switch_opener(opener) so it is defined outside
    ball_dropper_rect.center = (175,250)
    play_rect.center = (250,350)
    DISPLAYSURF.blit(txt_ball_dropper, ball_dropper_rect)
    DISPLAYSURF.blit(txt_play, play_rect)

def switch_opener(opener):
    if play_rect.collidepoint(pygame.mouse.get_pos()):
        opener = 'false'
    else:
        opener = 'true'
    return opener

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

def update_ball():
    DISPLAYSURF.blit(BALL, (ballob.rect.x,ballob.rect.y,30,30))

while True:
    DISPLAYSURF.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and opener == 'true':
            opener = switch_opener(opener)
        else:
            if event.type == KEYDOWN:
                if event.key == 'K_LEFT':
                    ballob.move_left()
                if event.key == 'K_RIGHT':
                    ballob.move_right()

    if opener == 'true':
        opening_screen()

    else:
        hoop_move()
        update_hoop()

        direction = switch_direction(direction)

        ballob.move_down()
        update_ball()

    pygame.display.update()
    fpsClock.tick(FPS)
