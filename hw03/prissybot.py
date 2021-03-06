#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.

# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults

name=raw_input("Enter your name: ")
print "PrissyBot: Hello there, "+name+"."
greeting=raw_input(name + ": ")
#print "PrissyBot: You mean, \""+greeting+", sir!\"" #A backslash is used to escape characters that otherwise have a special meaning.
num=int(3)
print "You mean '%s', SIR! %i" % (greeting,num)
print "PrissyBot: Tell me, what\'s your mother\'s name?"
mom=raw_input(""+name+": ")
print "PrissyBot: I knew a lady named "+mom+" once. She had a real ugly kid, though. You got any kids, "+name+"?"
raw_input(""+name+": ")
print "PrissyBot: Yeah cool whatever. How old are you, "+name+"?"
age=raw_input(""+name+": ")
age=int(age)
x=int(74-age)
y=float(74.0/age)
print "PrissyBot: Morgan Freeman is",x,"years older than you. You are",y,"times younger than Morgan Freeman. Who are you trying to fool, "+name+"?"
response=raw_input(""+name+": ")
print "PrissyBot:",(" "+response+"!")*6, "That's what you sound like."
print "PrissyBot: On a scale of 1 to 10, how annoying are you?"
scale=raw_input(""+name+": ")
scale=int(scale)
s=int(10-scale)
print "PrissyBot: Add",s,"to that, and you're spot on."
print "PrissyBot: Before you go, give me a character and I'll draw you a picture with it."
s=" "
c=raw_input("Enter a character: ")
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

