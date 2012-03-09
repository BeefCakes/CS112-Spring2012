#!/usr/bin/env python

import pygame
from pygame import draw
from pygame.locals import *
import random
import math

##constants
BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,0,255
GREEN = 0,255,0
PURPLE = 128,0,128
MAROON = 128,0,0
BLUEGREEN = 0,128,128
GREY1 = 150,150,150
GREY2 = 200,200,200

##game grid
grid = []
mines = []
locations = []
tiles = []
flags = []
covers = []

def nearby(listy, index):
    near = 0 #how many mines nearby
    #detect mine above
    if listy[(index-1)][2] == 1 and index%10 !=0: 
        near +=1 #increase the nearby mine counter
    #detect mine below
    if index < 99 and listy[(index+1)][2] == 1 and (index-9)%10 !=0: 
        near +=1
    #detect left
    if index < 90 and listy[(index+10)][2] == 1:
        near +=1
    #detect lower right
    if index < 89 and listy[(index+11)][2] == 1 and (index-9)%10 != 0:
        near +=1
    #detect upper left
    if index < 91 and listy[(index+9)][2] == 1 and index%10 != 0:
        near +=1
    #detect right
    if index > 9 and listy[(index-10)][2] == 1: 
        near +=1
    #lower left
    if index > 9 and listy[(index-9)][2] == 1  and (index-9)%10 != 0:
        near +=1
    #upper left
    if index > 11 and listy[(index-11)][2] == 1 and index%10 != 0:
        near +=1
#the third part of each list element stores the amount of nearby mines
    listy[index][3] = near 

for i in range(10): #10 is the size of the board
    row = []
    for j in range(10):
        row.append([i+1,j+1])
    grid.append(row)

while len(mines) < 10: #stops creating mines once there are 10
    m_row = random.randint(0,9) #row of mine
    m_col = random.randint(0,9) #column of mine
    mines.insert(0,[m_row, m_col]) #adds mine to beginning of mines list
    grid[(mines[0][0])][(mines[0][1])] = "M"

for i,row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "M":
            val = [i+1,j+1,1,0]
           # val = [i, j, 1, 0]
            locations.append(val)
        else:
            val = [i+1,j+1,0,0]
           # val = [i, j, 0, 0]
            locations.append(val)
        print val,  
    print ""

#print locations

for i in range(len(locations)):
    nearby(locations, i)

##functions and stuff

##initialize
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Minesweeper - press space to begin/reset")
clock = pygame.time.Clock()
bounds = screen.get_rect()
##setup game objects

#fonts
bigfont = pygame.font.Font(None, 30) #defines font and font size
smallfont = pygame.font.Font(None,25)


clicked = False
flagged = False
unflagged = False
#individual tile
def draw_tile(element): #takes a list element, splits it into parts, draws it
    x = element[0]
    y = element[1]
    bomb = element[2]
    near = str(element[3]) #nearby mines converted to string, to be drawn
    x *= 50
    y *= 50
  #  x *= 20
  #  y *= 20
    color = GREEN
   # clicked = False
   # rect = pygame.Rect((0,0), (50,50))
    rect = pygame.Rect((0,0), (50,50))
    tiles.append(rect)
    rect.center = (x+2, y+2)
  #  print rect.center
    ##text colors
    if near == "0":
        color = GREY1
    if near == "1":
        color = BLUE
    elif near == "2":
        color = GREEN
    elif near == "3":
        color = RED
    elif near == "4":
        color = PURPLE
    elif near == "5":
        color = MAROON
    elif near == "6":
        color = BLUEGREEN
    elif near == "7":
        color = BLACK
    elif near == "8":
        color = GREY2
    if bomb == 1:
        #outline
        draw.rect(screen, BLACK, (x, y, 50, 50)) 
        draw.rect(screen, GREY1, (x+2, y+2, 46, 46))
        #draw bomb
        draw.circle(screen,BLACK,(x+25,y+25),10)
    else: 
        #outline:
        draw.rect(screen, BLACK, (x, y, 50, 50))                            
        draw.rect(screen, GREY1, (x+2, y+2, 46, 46))
        #number displayed:
    
        title = smallfont.render(near, True, color)
        loc = title.get_rect()
        loc.center = (x+25,y+25)
        screen.blit(title, loc)
        
    if rect != clicked:
       # draw.rect(screen, BLACK, (x, y, 50, 50))                            
        #sort the covers list and remove duplicates
        covers.append([x+2, y+2, 46, 46])
        covers.sort()
        lastcover = covers[-1]
        for i in range(len(covers)-2, -1, -1):
            if lastcover == covers[i]:
                del covers[i]
            else:
                lastcover = covers[i]
        if flagged == rect:
            ##draw flag
          #  while len(flags) < 1:
            flags.append([x+23, y+10, 10, 10])
            #sort the flags list and remove duplicates
            flags.sort()
            lastflag = flags[-1]
            for i in range(len(flags)-2, -1, -1):
                if lastflag == flags[i]:
                    del flags[i]
                else:
                    lastflag = flags[i]
            print flags
            print "shit got flagged, son"

    if rect == clicked and flagged != rect:
       eject = covers.index([x+2, y+2, 46, 46])
       del covers[eject]
       if bomb == 1:
           draw.rect(screen, RED, (x+5, y+25, 40,5))
        # covers.append([x+50, y+50, 46, 46])
  #  elif unflagged == True:
   #     flags.remove([x+23, y+10, 10, 10])

    return bomb

done = False
game = False
while not done:
##input
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        #game commences when space is pressed
        elif event.type == KEYDOWN and event.key == K_SPACE:
            game = True
            
        elif event.type == MOUSEBUTTONDOWN:
         #   for rect in tiles:
            for rect in tiles:
                if event.button == 3:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        flagged = rect
                if event.button == 1:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        clicked = rect
                  #  elif rect.collidepoint(pygame.mouse.get_pos()) and bomb == 1
                       # done = True

       # elif event.type == MOUSEBUTTONUP:
        #    clicked = False
                
        pygame.draw.rect(screen, RED, (200,200,250,250)) #test

        if game:
            #draw
            screen.fill(GREY1)
            for i in range(len(locations)):
                #draw_tile((locations[i]))
                draw_tile((locations[i]))
            for i in range (len(covers)):
                draw.rect(screen, GREY2, covers[i])
                print covers[i]
            for i in range(len(flags)):
                draw.rect(screen, RED, flags[i])

         #   print clicked
##refresh
        pygame.display.flip()
        clock.tick(60)
