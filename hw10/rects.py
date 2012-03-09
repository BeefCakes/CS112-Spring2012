#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect

    "check if polygon is within rectangle"
"""
import pygame
from pygame import Rect
from pygame.locals import *

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    poly = list(poly) #polygon input becomes a list
    x, y, x2, y2 = rect
    poly_x = [] #a list for all the x-values in polygon
    poly_y = [] #a list for all the y-values in polygon
    contained = False #boolean for whether rect is within poly
    print poly
    print rect
#this loop goes though poly and adds the x and y values from each tuple to a seperate list, then sorts those lists
    for i in range(len(poly)):
        poly_x.append(poly[i][0])
        poly_x.sort()
        poly_y.append(poly[i][1])
        poly_y.sort()
 #if the highest or lowest values from poly_x or poly exceed the rect boundaries, the polygon is not entirly contained
    if poly_x[0] < x or poly_x[-1] > x2 or poly_y[0] < y or poly_y[-1] > y2:
       contained = False
    else: #i.e., if polygon values do not exceed rectangle
       contained = True
    return contained

poly_in_rect(((40, 80), (30, 80), (120,160), (500, 60)), (11, 20, 300, 500)) 

# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect
"""
##constants
BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,0,255
SCREEN_SIZE = 800,600
screen = pygame.display.set_mode(SCREEN_SIZE)
"""
def surround_poly(poly):
    poly = list(poly)
    poly_x = []
    poly_y = []
   # print poly
    for i in range(len(poly)):
        poly_x.append(poly[i][0])
        poly_x.sort()
        poly_y.append(poly[i][1])
        poly_y.sort()
    left = (poly_x[0]) #left is the lowest x point in polygon
    top = (poly_y[0])  #top is the lowest y point in polygon
#width is the greatest x point in polygon minus the lowest
    width = (poly_x[-1] - left) + 1
#height is the greatest y point in polygon minus the lowest
    height = (poly_y[-1] - top) + 1

    return pygame.Rect(left, top, width, height)
