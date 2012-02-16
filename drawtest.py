#!/usr/bin/env python

import pygame
from pygame.locals import *
#settings

BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
size = 400,400

THICKNESS = 20
#initialize
pygame.init() 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("draw test")

#Draw
screen.fill(BLACK)
#pygame.draw.rect(screen,BLUE,50,20)
pygame.draw.circle(screen,RED,(60,90),30,20)

#Loop
done = False
move = 8
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
        
        pygame.display.flip()




