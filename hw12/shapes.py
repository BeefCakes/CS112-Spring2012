# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     

import math

class Shape(object):
#    def __init__(self):
        
    def area(self):
        pass

    def perimeter(self):
        pass

class Rect(Shape):
    def __init__(self, x, y):
        self.x = x #width
        self.y = y #height

    def area(self):
        return self.x * self.y #area = width*height
    
    def perimeter(self):
        return (self.x * 2) + (self.y * 2) #perimeter = width*2 + height*2

class Square(Rect):
    def __init__(self, x):
        self.x = x
        self.y = x

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return (math.pi) * (self.r**2)
    
    def perimeter(self):
        return 2 * math.pi * self.r

rect1 = Rect(3,4)
sq = Square(5)
circ = Circle(3)

print rect1.x, rect1.y
print rect1.area()
print rect1.perimeter()
print sq.x
print sq.area()
print circ.area()
print circ.perimeter()

# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
