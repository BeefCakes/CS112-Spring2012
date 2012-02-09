#!/usr/bin/env python

import pygame

screen_size = 640,480
background = 0,0,0 #amount of red, green, blue (255 is the max)

#initiates pygame
pygame.init()
screen =pygame.display.set_mode(screen_size)

while True: #an infinite loop
    screen.fill(background)
    pygame.display.flip()
