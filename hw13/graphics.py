#!/usr/bin/env python

import pygame

#player ship
"""
def draw_player(surf, color):
    rect = surf.get_rect() #what does this do?
    
    d = min(rect.width, rect.height)

    pygame.draw.rect(surf, color, (0,0, (d/8), rect.height))
"""

def draw_player(surf, x, y):
    YELLOW = (255,255,0) #yellow
    rect = surf.get_rect() #returns a rectangle covering the surface

    d = min(rect.width, rect.height)

    pygame.draw.rect(surf, YELLOW, (x, y, (d/8), rect.height)) 
    
