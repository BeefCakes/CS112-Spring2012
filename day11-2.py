#!/usr/bin/env python

##multidimensional array

grid = []
for i in range(10): #number of rows
    row = []
    for j in range(10):  #number of columns
        row.append(0)
    grid.append(row)

print grid

for i,row in enumerate(grid):
    for j, val in enumerate(row):
        print val,
    print ""

