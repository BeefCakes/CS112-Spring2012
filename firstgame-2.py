#!/usr/bin/env python

#voodoo
import pygame
from pygame.locals import *

screen_size = 640,480
background = 0,0,0 #amount of red, green, blue (255 is the max)

#initiates pygame
pygame.init()
screen =pygame.display.set_mode(screen_size)

done=False #so that we don't get an infinite loop
while not done:
    event = pygame.event.poll() #listens to your input

    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE: #quits using escape key
        done = True
    elif event.type == KEYDOWN and event.key == K_w: #changes screen using w key
        background=255,255,255
    elif event.type == MOUSEBUTTONDOWN:
        print "Mouse",pygame.mouse.get_pos() #gets the mouse position

    screen.fill(background)
    pygame.display.flip()

print "Byebye"
