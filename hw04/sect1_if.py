#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-------------------------"

# 1.  Is n even or odd?
n=0
while n <= 0:
    n = raw_input("Enter a number: ")
    n = int(n)

if n%2 == 0:
    print "1. Number is even."
else:
    print "1. Number is odd."


# 2. If n is odd, double it
if n%2 != 0:
    print "2. Number doubled =",n*2
else:
    print "2. Not odd"


# 3. If n is evenly divisible by 3, add four
if n%3 == 0:
    print "3. Number + 4 =",n+4
else:
    print "3. Not evenly divisible by 3."
# 4. What is grade's letter value (eg. 90-100)
grade=0
while grade <=0 or grade >100:
    grade = raw_input("Enter a grade [0-100]: ")
    grade = int(grade)

if grade <=59:
    print "4. F"
elif grade >=60 and grade <=69:
    print "4. D"
elif grade >=70 and grade <=79:
    print "4. C"
elif grade >=80 and grade <=89:
    print "4. B"
elif grade >=90 and grade <=100:
    print "4. A"


