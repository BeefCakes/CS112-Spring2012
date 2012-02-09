#!/usr/bin/env python

TAs = ["Alec","Jack","Jonah"] #added later, a list
name_in=raw_input("enter a name: ")

if name_in == "Paul":
    print "you are cool"
elif name_in in TAs: #originally:   elif name_in == "Alec" or name_in == "Jonah" or name_in == "Jack":
    print "you smell bad"
else:
    print "you need some learning"
