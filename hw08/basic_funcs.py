#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    name = str(name)
    name2 = [] #creates secondary list for lower case
#converts each letter to lower case and appends it to secondary list
    for i in name:
        name2.append(i.lower()) 
    delimeter = "" #for use in joining name2
    print "hello,",
    return delimeter.join(name2)

print greeter("Cupcakes")
print greeter(2)

# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    shape = [] #creates a list for the box components
    delimeter = ""
    done = 0
    if w >= 2:
        horiz = "+" + "-"*(w-2) + "+\n"
        vert = "|" + " "*(w-2) + "|\n"
    else:
        horiz = "+\n"
        vert = "|\n"
    while done >= 0:
        if int(w) == False or int(h) == False or h < 1 or w < 1:
            print "Error: Invalid Dimensions"
            done = 1

        shape.insert(0, horiz)

        if h >=2:
            shape.append(horiz)
        if h >= 3:
            shape.insert(1, vert*(h-2))

        return delimeter.join(shape)

user_w = int(raw_input("Enter width: "))
user_h = int(raw_input("Enter height: "))
print box(user_w, user_h)



# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()

