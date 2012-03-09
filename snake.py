#!/usr/bin/env python
"""
 Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from random import randint
from pygame.locals import *

#Colors
BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,0,255
GREEN = 0,128,0

p1_x, p1_y = 0,0 #location of player 1
p1_dx, p1_dy = 0,0 #directions of player 1


#list for the player's position to be added to
pos1 = []
dotpos = [] #dot position

def draw_p1(pos1): #draws player 1
    x,y = pos1
    draw.rect(screen, GREEN, (x, y, 15, 15))

def move(x, y, dx, dy, bounds):
    x+=dx #direction x is added to x position
    y+=dy #direction y is added to y position
#if either player exceeds the screen bounds, they lose
    if x<bounds.left or x>bounds.right or y<bounds.top or y>bounds.bottom:
#movement halts
        dx=0 
        dy=0
        y=-30
        x=-30
    return x, y, dx, dy

def draw_dot(dotpos): #draws dot to be eaten
    x,y = dotpos

    draw.rect(screen, (fade,0,0), (x, y, 15, 15))

    

pygame.init()
screen = pygame.display.set_mode((800,600)) #screen size
pygame.display.set_caption("Snake - Press space to begin/reset")
clock = pygame.time.Clock()
done = False
game = False
screen_bounds = screen.get_rect() #sets screen size as bounds
trail1 = [] #list for p1's trail
trail_size = 30
score = 0
s = 1 #speed
fade = 4
f = 10

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
            trail_size = 30 #trail size resets to 30
            s = 1 #speed resets to 1
            score = 0 #score resets to 0
            p1_dx, p1_dy = 3*s,0 #p1 moves right at game start
#starting locations for p1 and p2
            p1_x, p1_y = 200,300 
            dotpos.append([randint(25,775), randint(25,575)])

    if game:
#player 1 controls (WASD)
#"!=" statements ensure that player cannot halt movement
        if event.type == KEYDOWN and event.key == K_w and p1_dy != 3*s:
            p1_dx, p1_dy = 0,-3*s #move north
        elif event.type == KEYDOWN and event.key == K_d and p1_dx != -3*s:
            p1_dx, p1_dy = 3*s,0 #east
        elif event.type == KEYDOWN and event.key == K_s and p1_dy != -3*s:
            p1_dx, p1_dy = 0,3*s #south
        elif event.type == KEYDOWN and event.key == K_a and p1_dx != 3*s:
            p1_dx, p1_dy = -3*s,0 #west

        screen.fill(BLACK) #black background, automatically refreshes

        fade+=f
        if fade > 250 or fade < 5:
            f *=-1
       
#movement of p1 and p2
        p1_x, p1_y, p1_dx, p1_dy = move(p1_x, p1_y, p1_dx, p1_dy, screen_bounds)
#player locations are appended to the trail lists
        trail1.append([p1_x, p1_y])
#player locations also added to seperate lists
        pos1.append([p1_x, p1_y])
#draw p1 trail
        if len(trail1)>trail_size:
            trail1.pop(0)
        for i in range(len(trail1)):
            draw_p1(trail1[i])
      
        draw_dot(dotpos[-1])
       

#if the newest value of pos1 matches a value in trail1 (i.e., if line intersects trail), round ends and must be reset
        
        if pos1[-1][0] >= (dotpos[-1][0]-15) and pos1[-1][0] <= (dotpos[-1][0]+15) and pos1[-1][1] >= (dotpos[-1][1]-15) and pos1[-1][1] <= (dotpos[-1][1]+15):
            dotpos.append([randint(25,775), randint(25,575)])
            trail_size +=5
            score +=1
            if score%3 == 0 and score > 0:
                s += .1

        if (pos1[-1] in trail1[:-1]):
            game = False
            dx=0 #movement halts
            dy=0
            print "GAME OVER \nScore:", score

    pygame.display.flip()
    clock.tick(60)

