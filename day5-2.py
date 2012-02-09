#!/usr/bin/env python

names=['bob','fred']

letters = ['a','d','f']
letters[1:1] = ['b','c']
print letters

letters = ['a','d','f']
letters += ['b','c'] #concatenates
print letters

letters = ['a','d','f']
letters += ['b','c']
print letters
print letters[-1] #prints the last element of the list (-2 would print second to last)

letters = ['a','d','f']
letters += ['b','c']
print letters
print letters[-1]
letters2 = letters[:]
letters[0] = 'huh'
print letters2
