#!/usr/bin/env python

#english to spanish dictionary
eng2sp = {} 
eng2sp["one"] = "uno"
eng2sp["two"] = "dos"
for k,v in eng2sp.items(): #k = key, v = value
    print k,v

#can be placed over multiple lines, for easier readability
people = {"Jonah" : "stupid",
          "Alec" : "smelly", 
          "Jack" : "ugly", 
          "Paul" : "awesome"}

name = raw_input("Your name: ")
if name in people: #if input is in the people dictionary
    print name,"is",people[name] #ex: "Alec is smelly"
else:
    print "I don't know you,",name

print len(people)
print people.keys()
print people.values()
