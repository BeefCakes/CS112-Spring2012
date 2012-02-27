#!/usr/bin/env python

#converting farenheit to celsius

def ftoc(temp):
    cent = temp-32
    cent*=5
    cent/=9
    return cent #returns the value.

num = int(raw_input("enter a temperature in farenheit: "))
print "in celsius that is: ",ftoc(num)
