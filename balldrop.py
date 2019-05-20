#necessary stuff
import pygame, sys, time, random
from pygame.locals import *
from ball import Ball
from hoop import Hoop
from obstacle import Obstacle
pygame.init()

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
#making the screen and FPS
DISPLAYSURF = pygame.display.set_mode((300,400), 0, 32)
FPS = 15
fpsClock = pygame.time.Clock()

#importing and changing the size of the hoop and ball images
HOOP = pygame.image.load('Basketball Hoop.png')
HOOP = pygame.transform.scale(HOOP, (45,45))
BALL = pygame.image.load('Basketball.png')
BALL = pygame.transform.scale(BALL, (30,30))

#naming the pop up screen
pygame.display.set_caption("Ball Drop")

#making the ball and hoop objects
ballob = Ball(135,30)
hoopob = Hoop(130)

#sprite group for all the obstacles
obstacles = pygame.sprite.Group()

#variable to keep track of which direction the hoop is moving
direction = 'right'

#variable to keep track of which level it is
level = 1

#rect for the 'play' text in the opening screen, also used as a button so it has to be defined outside the function
play_rect = DISPLAYSURF.get_rect()

#variable keeping track of if the round has been won or lost
win_lose = 'N/A'
#variable keeping track of if the opening screen has been exited yet
opener = 'true'

def opening_screen():
    BASICFONT = pygame.font.Font('freesansbold.ttf', 40)
    small_BASICFONT = pygame.font.Font('freesansbold.ttf', 22)
    txt_ball_dropper = BASICFONT.render('Ball Dropper',1,BLACK)
    txt_play = BASICFONT.render('Play',1,BLACK)
    txt_how_to1 = small_BASICFONT.render('Get the ball in the hoop',1,BLACK)
    txt_how_to2 = small_BASICFONT.render('without hitting the obtacles',1,BLACK)
    ball_dropper_rect = DISPLAYSURF.get_rect()
    #play_rect would be defined here but it is used in switch_opener(opener) so it is defined outside
    how_to_rect1 = DISPLAYSURF.get_rect()
    how_to_rect2 = DISPLAYSURF.get_rect()
    ball_dropper_rect.center = (175,250)
    play_rect.center = (250,350)
    how_to_rect1.center = (180,450)
    how_to_rect2.center = (158,475)
    DISPLAYSURF.blit(txt_ball_dropper, ball_dropper_rect)
    DISPLAYSURF.blit(txt_play, play_rect)
    DISPLAYSURF.blit(txt_how_to1,how_to_rect1)
    DISPLAYSURF.blit(txt_how_to2,how_to_rect2)

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
    obstacles.add(obstacleob)

def obstacle_collide():
    for obstacleob in obstacles:
        if obstacleob.rect.colliderect((ballob.rect.x,ballob.rect.y-30,30,30)):
            win_lose = 'lose'
            return True
    else:
        return False

def obstacle_mover():
    for obstacleob in obstacles:
        if obstacleob.side_moves2 != 0:
            if obstacleob.direction == 'left':
                obstacleob.move_left()
            if obstacleob.direction == 'right':
                obstacleob.move_right()

def update_obstacle():
    for obstacleob in obstacles:
        pygame.draw.rect(DISPLAYSURF,BLACK,obstacleob.rect,0)

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
            update_obstacle()

        if level == 3:
            obstacle_mover()
            update_obstacle()

        if level == 4:
            obstacle_mover()
            update_obstacle()

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
                if level == 2:
                    obstacle_maker(125,220,50,20,0,'right')
                if level == 3:
                    obstacle_maker(135,210,30,10,12,'either')
                if level == 4:
                    obstacle_maker(145,160,10,30,18,'left')
                    obstacle_maker(145,210,10,30,18,'right')
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
