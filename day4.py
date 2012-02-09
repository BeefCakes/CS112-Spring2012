#!/usr/bin/env python

count=0 #these first two lines make sure that user can't enter a negative number
while count <=0:
    count=raw_input("Count down from: ")
    count=int(count)

while count>0:
    print count
    count-=1

print "Blastoff!"
