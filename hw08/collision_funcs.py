#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

# def point_in_box(pt, box):

def point_in_box(pt, box):
    x1,y1 = pt
    x,y,w,h = box
    print "point is", pt
    print "box is", box
    if x1 < x or y1 < y or x1 > (x + w) or y1 > (y + h):
        inside = False
    else:
        inside = True
    print "Point inside box:", inside
        
point_in_box((5,7), (2,2,100,100))
