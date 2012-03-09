#!/usr/bin/env python

import pygame
from pygame.locals import *

#globals
BACKGROUND = 80, 80, 80 #grey background. All caps because it is a constant.
SCREEN_SIZE = 800, 600 #a tuple
FPS = 30 #frames per second
RECT_SIZE = 120, 80 #a tuple

#initialize
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

#setup game objects
bounds = screen.get_rect()

rect = pygame.Rect((0,0,), RECT_SIZE)
rect.center = bounds.center
grabbed = False

clock = pygame.time.Clock()
done = False
while not done:
    #input
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            #makes sure mouse is in the rectangle
            if rect.collidepoint(pygame.mouse.get_pos()):
                grabbed = True
        elif evt.type == MOUSEBUTTONUP:
            grabbed = False

    if grabbed:
        rect.center = pygame.mouse.get_pos()
        rect.clamp_ip(bounds)

    #draw
    screen.fill(BACKGROUND) #redraws screen
    pygame.draw.rect(screen, (255,0,0), rect)
    pygame.draw.rect(screen, (0,0,0), rect, 5) #5 is the width
    
    #refresh
    pygame.display.flip()
    clock.tick(FPS)
