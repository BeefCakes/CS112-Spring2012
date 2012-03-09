# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#
import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        dx = self.x - other.x #distance between first x and second x
        dy = self.y - other.y #between first y and second 7
        return int(math.sqrt(dx**2 + dy**2)) #pythagoras, y'all

    def move(self, x, y):
        self.x = x #resets self.x to the new x
        self.y = y #resets self.y to new y
        return self.x, self.y

    def translate(self, x, y):
        self.x += x #new x is added to self.x
        self.y += y #new y is added to self.y
        return self.x, self.y
    
pt1 = Point(2,5)
pt2 = Point(7,12)

print pt1.distance(pt2)
print pt1.move(14,17)
print pt1.translate(2,2)


# Advanced Section:
# ---------------------------------------
# Add the following function:
#     slope(self, other):
#         calculate the slope between two points
#
#     extrapolate(self, slope, distance):
#         returns a point along the line defined by slope
#         a given distance away
#
# Also, add the following special python methods:
#     __eq__(self, other):
#         checks if other is a Point and is equal to self
#
#     __str__(self):
#         returns a string representation of the point 
#     
#     >>> print Point(3,4)
#     (3,4)
#     >>> a = Point(1,2)
#     >>> b = Point(1,2)
#     >>> print a == b
#     True
