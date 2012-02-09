#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

print "1. Sum of",sum(nums)


# 2. Print every even number in nums

print "2. Even numbers:",
evens = []
for i in nums:
    if i%2 == 0:
        evens.append(i)
print evens

#CODE GOES HERE

# 3. Does nums only contain even numbers? 
for i in nums:
    if i%2 !=0:
        only_even = False
    else:
        only_even = True
#CODE GOES HERE

print "3.",
if only_even:
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
odds = []
print "4. Every odd number under 100:", 
for i in range(100):
    if i%2 !=0:
      odds.append(i)
print odds
