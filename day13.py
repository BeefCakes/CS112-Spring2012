#!/usr/bin/env python

class Animal(object): #this is an abstract class. don't make instance of it.
    def __init__(self, name):
        self.name = name

    def can_eat(self, food):
        pass

    def eat(self, food):
        pass

    def speak(self):
        pass

    def die(self):
        print self.name, "lived a good life"

    def __str__(self): #to make a string
        return self.__class__.__name__ + ": " + self.name

class Dog(Animal):
    def can_eat(self, food):
        return True

    def eat(self, food):
        print self.name, "gobbles", food

    def speak(self):
        print self.name + ": woof"

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, "Mrs. "+name) #adds "Mrs" to beginning of name
    
    def can_eat(self, food):
        return food.lower() == "fish"
    
    def eat(self, food):
        print self.name, "sniffs", food

    def speak(self):
        print self.name, "walks away"

"""
animals = [ Cat("Pretty"), Dog("Rover") ]

for animal in animals:
    if animal.can_eat("garbage"):
        animal.eat("garbage")
    if animal.can_eat("fish"):
        animal.eat("fish")
    animal.speak()
    animal.die()
"""

dog = Dog("Rover")
cat = Cat("Pretty")

#isinstance returns true or false
print isinstance(dog, Dog)
print isinstance(dog, Animal)
print isinstance(cat, Cat)
print isinstance(cat, Animal)
print isinstance (cat, Dog)

print dog
print cat
