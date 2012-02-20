#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm

NOTE- It took me four hours to figure out this program, and seeing as it's now 1 AM, I'm just going to submit it and ignore sort.py for now. I'm willing to accept a half-grade or whatever.

-Jordan

"""
from hwtools import input_nums

#recieves a list of numbers from user (as defined in hwtools.py)
nums = input_nums() 
nums.sort() #sorts numbers from low to high
print nums #displays the sorted list
print "I have sorted your numbers."
#obtains integer to search for from user
input_value = int(raw_input("Which number should I find: ")) 
#the max and min index variables are used to alter the mid variable
min_index = 0
max_index = len(nums)-1
#the while loop continues as long as the remaining array has not been reduced to zero
while max_index >= min_index:
    mid = (max_index + min_index)/2 #defines the middle of the array
    print "min index =", min_index
    print "max index =", max_index
    print "middle element =", nums[mid]
    if nums[mid] == input_value: #if middle value is input value
        break
#if the middle element of nums is greater than input value
    elif nums[mid] > input_value: #if middle is greater than input
#the max is redefined as being one less than the middle element, thus shifting the sub-array to the left of the middle element
        max_index = mid -1
        print "middle element is greater than value, shifting to left."
    elif nums[mid] < input_value: #if middle is less than input
        min_index = mid + 1 #sub-array shifts to the right
        print "middle element is less than value, shifting to right."

if nums[mid] == input_value: #if the middle element equals the input
#displays the user input and the index at which it is located in the sorted array
    print "Found", input_value,"at", mid, 

else: #i.e., if middle element is not input
    print "Could not find", input_value
