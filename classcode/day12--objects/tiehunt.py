#!/usr/bin/env python

import math
import random
from random import randrange

import pygame
from pygame.locals import *


## Settings
C_BLACK = 0,0,0
C_RED = 255,0,0


## from tiefighter.py
def draw_tie(surf, color, size):
    wall = size / 8

    surf.fill(C_BLACK)
    pygame.draw.rect(surf, color, (0, 0, wall, size))
    pygame.draw.rect(surf, color, (size-wall, 0, wall, size))
    pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
    pygame.draw.circle(surf, color, (size/2, size/2), size/4)

class TieFighter(object):
    #vx and vy are velocity    
    def __init__(self, x, y, vx, vy, bounds, color, size = 40): #predefined values must go at end
      #  self.x=x
      #  self.y=y
        self.vx=vx
        self.vy=vy
        self.size=size
        self.color=color
        self.bounds = bounds

        self.image = pygame.Surface((size, size))
        draw_tie(self.image, color, size)
        
        self.rect = pygame.Rect(x, y, size, size)
        
    def update(self):
        self.rect.x += self.vx #adds vx to x each time it updates
        self.rect.y += self.vy
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx *= -1
            self.rect.x += self.vx*2
        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy *= -1
            self.rect.y += self.vy*2
                
    def draw(self, surf):
        surf.blit(self.image, self.rect)

class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)
        self.ties = [] #creates a list for tie fighters

      #  self.ties.append(TieFighter(200, 200, 3, 3, self.bounds)) #adds a tie fighter with a position of (200,200) and velocity of 3
      #  while len(self.ties) < 20:
          #  print len(self.ties)
         #   self.ties.append(TieFighter(rand_x, rand_y, rand_vx, rand_vy, self.bounds))
    
#rather than putting the done loop at end of program, this object runs itself
    def run(self): 
        clock = pygame.time.Clock()
        done = False
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    rand_x = random.randint(40,760)
                    rand_y = random.randint(40,560)
                    rand_vx = random.randrange(-3,4,2)
                    rand_vy = random.randrange(-3,4,2)
                    print rand_vy
                    rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    self.ties.append(TieFighter(rand_x, rand_y, rand_vx, rand_vy, self.bounds, rand_color))
                    if len(self.ties) > 100:
                        self.ties.pop(0)
            # update
            for tie in self.ties:
                tie.update()
            # draw
            self.screen.fill(C_BLACK)

            for tie in self.ties:
                tie.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__": 
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"

#if we wanted to import tiehunt from a different program, we wouldn't use "__main__"
