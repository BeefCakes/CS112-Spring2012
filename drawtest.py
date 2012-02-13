#!/usr/bin/env python

import pygame
from pygame.locals import *
#settings
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
size = 400,400
#initialize
pygame.init() 
screen = pygame.display.set_mode(size)

done = False
move = 8
pygame.key.set_repeat(100,100)
while not done:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            move += 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            move -= 1

#Draw
screen.fill(BLACK)
for i in range(0,400,move):
    pygame.draw.line(screen,BLUE,(45,189),(289,100),8)
    pygame.draw.line(screen,RED,(250,300),(23,150),8)

    pygame.display.flip()
