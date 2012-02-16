#!/usr/bin/env python

##Before:
"""
var1=0
var2=[]
var3=None
while var3!="":
    var3=raw_input()
    var2.append(float(var3))
for var in var2:
    var1+=var
print var1/len(var2)

"""

##After:

input_list=[]
input_number = None

#get list of numbers from user
while input_number != "":
    input_number = raw_input()
    if input_number.isdigit():
        input_list.append(float(input_number))

#total the list of numbers
total=0
for num in input_list:
    total += num

#print average of list
print total/len(input_list)
