#!/usr/bin/env python

import pygame
from pygame.locals import *

#globals
BACKGROUND = 80, 80, 80 #grey background. All caps because it is a constant.

RED = 255,0,0
WHITE = 255,255,255
GREEN = 0,255,0
PURPLE = 150,0,150

SCREEN_SIZE = 800, 600 #a tuple
FPS = 30 #frames per second
RECT_SIZE = 120, 80 #a tuple

#initialize
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

#setup game objects
bounds = screen.get_rect()

#creates a list of four rectangles
rects = [ pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE) ]

rects[0].topleft = bounds.topleft #sets the first rectangle to top left
rects[1].topright = bounds.topright #second triangle to top right
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright

#writing on screen
bigfont = pygame.font.Font(None, 80) #defines font and font size

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
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    grabbed = rect
#the clicked rectangle is added to the end of the list, making it on top
                if grabbed:
                    rects.remove(grabbed)
                    rects.append(grabbed)
        elif evt.type == MOUSEBUTTONUP:
            grabbed = None

    if grabbed:
        grabbed.center = pygame.mouse.get_pos()
        grabbed.clamp_ip(bounds)

    ##draw
    screen.fill(BACKGROUND) #redraws screen
    #draw text
    text = bigfont.render("Drag the rectangles", True, (0,0,0), BACKGROUND)
    loc = text.get_rect()
    loc.center = bounds.center
    screen.blit(text, loc)

    for rect in rects:
#"others" is a seperate list, so that rectangles don't collide with themselves
        others = rects[:] #copies all of rects into others
        others.remove(rect)
#when rectangle is grabbed, turns white
        if rect == grabbed:
            color = WHITE
#if rectangles overlap, turn purple
        elif rect.collidelist(others) != -1:
            color = PURPLE
        else:
            color = RED


        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 5) #5 is the width
    
    #refresh
    pygame.display.flip()
    clock.tick(FPS)
