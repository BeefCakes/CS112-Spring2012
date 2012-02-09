#!/usr/bin/env python

titles = ["Hitchhikers guide to the galaxy",
          "Restaurant at the end of the universe",
          "Life the universe and everything"]
titles.append("So long and thanks for all the fish")
titles.append("Mostly harmless")
for title in titles: #this is a FOR loop, telling each element to print in its own line
    print title 
for i in range(1,11,2): #prints numbers from 1 to 10, counting by 2
    print i
numbers = range(100)

for i,n in enumerate(numbers):
    numbers[i] = n*.2 #counts by .2
print numbers
