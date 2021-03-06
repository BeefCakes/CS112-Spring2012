#!/usr/bin/env python

import pygame
from pygame.locals import *
#settings
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
YELLOW = 255,255,0
size = 400,400
#initialize
pygame.init()
screen = pygame.display.set_mode(size)

done = False
sep = 8
pygame.key.set_repeat(100,100)
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            sep += 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            sep -= 1

    ##Draw
    screen.fill(BLACK)
    for i in range(0,400,sep):
        pygame.draw.line(screen,RED,(0,i),(i,399)) #(surface, color, start_pos, end_pos, width=1)
        pygame.draw.line(screen,GREEN,(i,399),(399,399-i)) 
        pygame.draw.line(screen,BLUE,(399,399-i),(399-i,0))
        pygame.draw.line(screen,RED,(399-i,0),(0,i))

    pygame.display.flip()
