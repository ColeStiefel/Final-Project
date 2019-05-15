import pygame, sys, time, random
from pygame.locals import *
from ball import Ball
from hoop import Hoop
from obstacle import Obstacle

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
DISPLAYSURF = pygame.display.set_mode((300,400), 0, 32)
FPS = 15
fpsClock = pygame.time.Clock()

HOOP = pygame.image.load('Basketball Hoop.png')
HOOP = pygame.transform.scale(HOOP, (45,45))

BALL = pygame.image.load('Basketball.png')
BALL = pygame.transform.scale(BALL, (30,30))

pygame.display.set_caption("Ball Drop")

ballob = Ball(135,30)
hoopob = Hoop(0)

obstacles = pygame.sprite.Group()

direction = 'right'

level = 1

play_rect = DISPLAYSURF.get_rect()

win_lose = 'N/A'
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

def game_over():
    BASICFONT = pygame.font.Font('freesansbold.ttf', 50)
    txt_game_over = BASICFONT.render('Game Over',1,BLACK)
    game_over_rect = DISPLAYSURF.get_rect()
    game_over_rect.center = (160,250)
    DISPLAYSURF.blit(txt_game_over, game_over_rect)

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
    DISPLAYSURF.blit(BALL, (ballob.rect.x,ballob.rect.y-30,30,30))

def round_over():
    if hoopob.rect.contains(ballob.rect):
        win_lose = 'win'
    else:
        win_lose = 'lose'
    return win_lose

def obstacle_maker(x,y,length,width,side_moves,direction):
    obstacleob = Obstacle(x,y,length,width,side_moves,direction)
    pygame.draw.rect(DISPLAYSURF,BLACK,obstacleob.rect,0)
    obstacles.add(obstacleob)

def obstacle_collide():
    if pygame.sprite.spritecollideany(ballob,obstacles):
        win_lose = 'lose'
        return True
    else:
        return False

def obsacle_mover():
    for obstacle in obstacles:
        if obstacle.side_moves2 != 0:
            if obstacle.side_moves1 != 0:


while True:
    DISPLAYSURF.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and opener == 'true':
            opener = switch_opener(opener)
        if event.type == KEYDOWN and opener != 'true':
            if event.key == K_LEFT:
                ballob.move_left()
            if event.key == K_RIGHT:
                ballob.move_right()

    if opener == 'true':
        opening_screen()

    else:
        hoop_move()
        update_hoop()

        direction = switch_direction(direction)

        ballob.move_down()
        update_ball()

        if level == 2:
            obstacle_maker(110,250,80,20,0,'right')

        if level == 3:
            obstacle_maker(130,225,40,20,8,'right')

        if ballob.rect.y == 355 or obstacle_collide() == True:
            win_lose = round_over()
            if win_lose == 'win':
                level += 1
                ballob.reset()
                hoopob.reset()
                direction = 'right'
                win_lose = 'N/A'
                FPS += 3
                for obstacleob in obstacles:
                    obstacles.remove(obstacleob)
            if win_lose == 'lose' or obstacle_collide() == True:
                while True:
                    DISPLAYSURF.fill(WHITE)
                    game_over()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
