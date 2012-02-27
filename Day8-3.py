#/usr/bin/env python

from random import randint
import pygame
from pygame import draw
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))

screen.fill((0,0,0)) #black color background
done = False

def draw_tie(surf, color, pos, size=40):
    x, y = pos
    width = size/8
    draw.rect(surf, color, (x,y,width,size)) #first vertical line
    draw.rect(surf, color, (x+size-width,y,width,size)) #second vertical line
    draw.rect(surf, color, (x,y+(size-width)/2,size,width)) #middle horizontal
    draw.circle(surf, color, (x+size/2,y+size/2), size/4) #circle

col = 200
dir = 1
#to ensure that shapes are stored after each refresh
color = []
pos = []
size = []
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE: #escape key
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            color.append((col,0,col))
            pos.append(pygame.mouse.get_pos())
            size.append(randint(20, 80)) #random size from 20 to 80

    #draw tie fighter
    col+=dir
    if col>255 or col<0:
        dir*=-1 #flips from negative to positive or vice versa
        col+=dir
    draw_tie(screen, (col,0,col), (20, 30))
    draw_tie(screen, (col,col,0), (200, 130))
    draw_tie(screen, (0,col,col), (300, 400))
    
    screen.fill((0,0,0)) #refreshing screen
    for i in range(len(color)-1,-1,-1):
        print i
        size[i]-=2 #tie fighters shrink
  #if tie fighter becomes too small, it is popped (removed) from list    
        if size[i]<=0:
            size.pop(i)
            pos.pop(i)
            pos.pop(i)
        else:
            draw_tie(screen, color[i], pos[i], size[i])
    pygame.display.flip()
    clock.tick(15)
