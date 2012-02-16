#!/usr/bin/env python
"""
prissybot2.py

CS112 Homework 6:   PrissyBot ROUND 2!

Code has been (hopefully) cleaned up, and attempts have been made to idiot-proof the program for a wider variety of user inputs

"""

name = raw_input("Enter your name: ") #Recieves user name
#addition symbol used to place variable amidst strings
print "PrissyBot: Hello there, "+name+"."
greeting=raw_input(name + ": ")

 #backslash used to escape characters that have a special meaning, allowing the variable to be placed here within quotation marks.
print "PrissyBot: You mean, \""+greeting+", sir!\""
print "PrissyBot: Tell me, what\'s your mother\'s name?"
mom = raw_input(name + ": ") #assigns user's mother's name to variable "mom"

print "PrissyBot: I knew a lady named "+mom+" once. She had a real ugly kid, though. You got any kids, "+name+"?"
raw_input(name + ": ") #user input is irrelevant here; PrissyBot ignores

print "PrissyBot: Yeah cool whatever. How old are you, "+name+"?"
#the following two lines ensure that user does not enter a negative number
age = 0
while age <= 0:
    age = int(raw_input("Your age: ")) #recieves an integer from user
if age < 74: #user is younger than 74
    younger = float(74.0/age) #divides 74 by user age and converts to float
    print "PrissyBot: Morgan Freeman is", (74 - age),"years older than you. You are", younger,"times younger than Morgan Freeman. Who are you trying to fool, "+name+"?" 

elif age > 74: #user is older than 74
    older = float(age/74.0) #divides user age by 74, converts to float
    print "PrissyBot: Morgan Freeman is", (age - 74),"years younger than you. You are", older,"times older than Morgan Freeman. How do you even know how to use a computer, "+name+"?"

else: #user is 74
    print "PrissyBot: Are you Morgan Freeman?"

response = raw_input(name + ": ")
#concatenates the user response 6 times, quite dickishly.
print "PrissyBot:", (response + "! ")*6 + "That's what you sound like." 
print "PrissyBot: On a scale of 1 to 10, how annoying are you?"
#the following two lines ensure that user does not enter a negative number
scale = 0
while scale <= 0: 
    scale = int(raw_input("Enter a Number [1-10]: ")) #recieves integer from user

#if user enters 10 or above, PrissyBot is glad to see that you agree with him.
if scale >= 10: 
    print "PrissyBot: Outstanding."
else: # i.e., if number is between 0-10
    print "PrissyBot: Add", (10 - scale), "to that, and you're spot on."
print "PrissyBot: Before you go, give me a character and I'll draw you a picture with it."
s = " " #assigns a variable to a space, for use in ASCII art
c = raw_input("Enter a character: ") #takes a character
#spaces added to beginning and end for visual clarity
print s 
print 6*s,8*c, 3*s,3*c, 5*s,3*c
print 6*s,8*c, 3*s,3*c, 5*s,3*c
print 6*s,3*c, 8*s,3*c, 5*s,3*c
print 6*s,8*c, 3*s,3*c, 5*s,3*c
print 6*s,8*c, 3*s,3*c, 5*s,3*c
print 6*s,3*c, 8*s,3*c, 5*s,3*c
print 6*s,3*c, 9*s,3*c, 3*s,3*c
print 6*s,3*c, 10*s,3*c, 1*s,3*c
print 6*s,3*c, 2*s,2*c, 6*s,5*c, 3*s,2*c
print s
print "PrissyBot: Bye now."




# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4
