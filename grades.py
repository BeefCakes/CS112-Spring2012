#!/usr/bin/env python

# 4. What is grade's letter value (eg. 90-100)
grade=0
while grade <=0 or grade >100:
    grade = raw_input("Enter a grade [0-100]: ")
    grade = int(grade)

if grade <=59:
    print "4. F"
elif grade >=60 and grade <=69:
    print "4. D"
elif grade >=70 and grade <=79:
    print "4. C"
elif grade >=80 and grade <=89:
    print "4. B"
elif grade >=90 and grade <=100:
    print "4. A"


