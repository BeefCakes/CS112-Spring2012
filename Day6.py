#!/usr/bin/env python

##Bad and good variable names

bob=1 #not descriptive
EIGHT=256 #don't use numbers as variable names
charmander = 'c' #just no
pi = pygame.Surface() #no, it could be confused with number pi
p_img = pygame.Surface() #No, still bad

player_image=pygame.Surface #YES! Makes sense
ply_img=pygame.Surface #this might work too

player_rect_for_collision = Rect() #No, too long

a=3 #you could maybe do this for temporary variables

BOB="Fred" #No. An all-caps variable should be a constant, like screen size.
Player=5 #No, first letter should not be capitalized (unless using an object, which we haven't gotten to yet)

##Typing long variables

longVariableNames
long_variable_names #preferred
longvariablenames #don't use this

##Multi-line comments

"""

This is a multi-line comment
Lots of stuff can be typed here
This is a string, although python ignores it


"""

##Spacing

t=x*3+y*3/2 #No. This works, but is confusing
t = x*3 + (y*3)/2 #Yes. This is the same, but easier to read

max(a,b)
max(a, b) #easier to read

