#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = 1
while num%3 != 0 or num <=0:
    num=raw_input("Enter a multiple of 3: ")
    num=int(num)

print "1.", num

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0


print "2. Countdown from", num
#CODE GOES HERE
while num>0:
    print " ",num,"..."
    num-=3
print" ",0

# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.

# num = int(raw_input("3. Countdown from: "))

num = 0
while num <=0:
    num = int(raw_input("3. Countdown from: "))
    num=int(num)
    if num%3 == 0:
        while num>0:
            print " ",num,"..."
            num-=3
        print" ",0
        break
    elif num%2 == 0:
        while num>0:
            print " ",num,"..."
            num-=2
        print" ",0
        break
    else:
        while num>0:
            print " ",num,"..."
            num-=1
        print" ",0
        break
