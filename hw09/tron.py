#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from pygame.locals import *

#Colors
BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,0,255

p1_x, p1_y = 0,0 #location of player 1
p1_dx, p1_dy = 0,0 #directions of player 1

p2_x, p2_y = 0,0 #location of player 2
p2_dx, p2_dy = 0,0 #location of player 2

#lists for the two players positions to be added to
pos1 = []
pos2 = []

score1 = 0 #player 1 score
score2 = 0 #player 2 score

def draw_p1(pos1): #draws player 1
    x,y = pos1

    draw.rect(screen, RED, (x, y, 5, 5))

def draw_p2(pos2): #draws player 2
    x2, y2 = pos2

    draw.rect(screen, BLUE, (x2, y2, 5, 5))

def move(x, y, dx, dy, bounds):
    x+=dx #direction x is added to x position
    y+=dy #direction y is added to y position
#if either player exceeds the screen bounds, they lose
    if x<bounds.left or x>bounds.right or y<bounds.top or y>bounds.bottom:
#movement halts
        dx=0 
        dy=0
        y=-5
        x=-5
    return x, y, dx, dy

pygame.init()
screen = pygame.display.set_mode((800,600)) #screen size
pygame.display.set_caption("Tron - Press space to begin/reset")
clock = pygame.time.Clock()
done = False
game = False
screen_bounds = screen.get_rect() #sets screen size as bounds
trail1 = [] #list for p1's trail
trail2 = [] #list for p2's trail
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
 #game commences when space is pressed
        elif event.type == KEYDOWN and event.key == K_SPACE:
            game = True
#both trails are reset
            del trail1[:]
            del trail2[:]
            p1_dx, p1_dy = 2,0 #p1 moves right at game start
            p2_dx, p2_dy = -2,0 #p2 moves left at start
#starting locations for p1 and p2
            p1_x, p1_y = 200,300 
            p2_x, p2_y = 600,300

    if game:
#player 1 controls (WASD)
#"!=" statements ensure that player cannot halt movement
        if event.type == KEYDOWN and event.key == K_w and p1_dy != 2:
            p1_dx, p1_dy = 0,-2 #move north
        elif event.type == KEYDOWN and event.key == K_d and p1_dx != -2:
            p1_dx, p1_dy = 2,0 #east
        elif event.type == KEYDOWN and event.key == K_s and p1_dy != -2:
            p1_dx, p1_dy = 0,2 #south
        elif event.type == KEYDOWN and event.key == K_a and p1_dx != 2:
            p1_dx, p1_dy = -2,0 #west

#player 2 controls (arrows)
        elif event.type == KEYDOWN and event.key == K_UP and p2_dy != 2:
            p2_dx, p2_dy = 0,-2
        elif event.type == KEYDOWN and event.key == K_RIGHT and p2_dx != -2:
            p2_dx, p2_dy = 2,0
        elif event.type == KEYDOWN and event.key == K_DOWN and p2_dy != -2:
            p2_dx, p2_dy = 0,2
        elif event.type == KEYDOWN and event.key == K_LEFT and p2_dx != 2:
            p2_dx, p2_dy = -2,0

        screen.fill(BLACK) #black background, automatically refreshes

#movement of p1 and p2
        p1_x, p1_y, p1_dx, p1_dy = move(p1_x, p1_y, p1_dx, p1_dy, screen_bounds)
        p2_x, p2_y, p2_dx, p2_dy = move(p2_x, p2_y, p2_dx, p2_dy, screen_bounds)
#player locations are appended to the trail lists
        trail1.append([p1_x, p1_y])
        trail2.append([p2_x, p2_y])
#player locations also added to seperate lists
        pos1.append([p1_x, p1_y])
        pos2.append([p2_x, p2_y])
#draw p1 trail
        for i in range(len(trail1)):
            draw_p1(trail1[i])
#draw p2 trail
        for i in range(len(trail2)):
            draw_p2(trail2[i])
#if the newest value of pos1 matches a value in trail1 (i.e., if line intersects trail), round ends and must be reset
        if (pos1[-1] in trail1[:-1]) or (pos1[-1] in trail2[:-1]):
            game = False
            dx=0 #movement halts
            dy=0
            score2 +=1
            print "Player 2 wins."
            print " Player 1:", score1,"\n Player 2:", score2 #prints player scores
#same as previous, but with pos2
        elif (pos2[-1] in trail2[:-1]) or (pos2[-1] in trail1[:-1]):
            game = False
            dx = 0
            dy = 0
            score1+=1
            print "Player 1 wins."
            print " Player 1:", score1,"\n Player 2:", score2

    pygame.display.flip()
    clock.tick(60)

