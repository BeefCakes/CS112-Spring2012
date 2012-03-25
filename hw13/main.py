#!/usr/bin/env python

import math

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from graphics import draw_player

class Ship(Sprite):
    width = 20
    height = 20
    def __init__(self):
        Sprite.__init__(self, x, y, vx, vy, bounds)
        
        self.vx = vy
        self.vy = vy
        self.bounds = bounds
        self.color = color

        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()
    
    def draw_image(self):
        self.image.fill(self.color)

    def update(self):
        pass

class Player(Ship):
    #starting position
    px = 200
    py = 200
    color = (255,255,0)
        
    def draw_image(self):
        draw_player(self.image, px, py)

me = Player

##GAME
class Game(Application):
    title = "shoot 'em up"
    screen_size = 800, 600

    def __init__(self):
        Application.__init__(self)

        self.bounds = self.screen.get_rect()

    def handle_event(self, event):
      #  if event.type == KEYDOWN and event.key == K_RIGHT:
            # move player
    
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print pygame.mouse.get_pos()

    def draw(self, screen):
        screen.fill((0,0,0))
        Player.draw_image(me)

if __name__ == "__main__":
    Game().run()
    print "ByeBye"
        
    
