#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)
pygame.draw.circle(screen,BLUE,(150,140),115,20) #blue circle
pygame.draw.circle(screen,BLACK,(400,140),115,20) #black circle
pygame.draw.circle(screen,RED,(650,140),115,20) #red circle
pygame.draw.circle(screen,YELLOW,(275,250),115,20) #yellow circle
pygame.draw.circle(screen,GREEN,(525,250),115,20) #red circle
#################################
##  DRAW OLYMPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
