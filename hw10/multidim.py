#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.
"""


# 1.  find_coins
#       find every coin (the number 1) in a givven room
#          room: a NxN grid which contains coins

#          returns: a list of the location of coind
#
#       Example:
#       0 0 0 1 0 0
#       0 0 1 0 0 0
#       0 0 0 0 1 0
#       0 0 0 0 0 0
# 
#       >>> find_coins(room)
#       [ [3, 0], [2, 1], [4, 2] ]
#      

import random

def find_coins(room):
   # rows, cols = room
    n = room
#    n = list(n)
    rows = n[0]
   # rows = int(rows)
    cols = n[1]
  #  cols = int(cols)
    print rows, cols
    print n
    grid = []
    coins = []
    print type(rows)
    for i in range(rows): #number of rows
        row = []
        for j in range(cols): #number of columns
                row.append(0)
        grid.append(row)

    print grid
    while len(coins) < 3: #once there are 3 coins, stop creating random x and y
        c_row = random.randint(1,rows) - 1
        c_col = random.randint(1,cols) - 1
        coins.insert(0,[c_row, c_col])
        grid[(coins[0][0])][(coins[0][1])] = 1

    ##print rows
    for i,row in enumerate(grid):
        for j, val in enumerate(row):
            print val,
        print ""
    print coins
    return coins

find_coins((6,7))

"returns a list of every coin in the room"


# 2. distance_from_player
#      calculate the distance from the player for each 
#      square in a room.  Returns a new grid of given
#      width and height where each square is the distance
#      from the player

import math

def distance_from_player(player_x, player_y, width, height):
    "calculates the distance of each square from the player"

    grid = []
    for i in range(width):
        row = []
        for j in range(height):
            row.append(0)
        grid.append(row)

    print grid
    grid[player_x][player_y] = "P"
    distances = []

    for i,row in enumerate(grid):
        a = i - player_x
        for j, val in enumerate(row):
            b = j - player_y
            if val == "P":
                distance = 0.0
                print val,
                distances.append(distance)
            else:
             #   distance = int(math.sqrt(a**2 + b**2))
                distance = math.sqrt(a**2 + b**2)
                print distance,
                distances.append(distance) 
#how do I get the rows as their own list elements?
        print ""

    print distances
    return distances

distance_from_player(0, 0, 6, 6)
