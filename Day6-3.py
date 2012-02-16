#!/usr/bin/env python

from random import randint
s=1

list_size=int(raw_input()) #recieves size of list from user
list=[]

#takes the lenth of inputted number, gives a list of random numbers (1-20) of that length
for _ in range(list_size): 
    list.append(randint(0,20))
print list
while s:
    s=0
    for var in range(1,list_size):
        if list[var-1]>list[var]:
            t1=list[var-1]
            t2=list[var]
            list[var-1]=t2
            list[var]=t1
            s=1
print list
