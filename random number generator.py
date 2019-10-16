# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:15:23 2019

@author: ramon
"""

print ("let's play a game")
print ("Let's see if you can guess the random number")

integer = input("Enter the number you think will be generated: ")

import random
for integer in range (1):
    print (random.random(1,10))

if integer <= random.random():
    print("Your guess was too low")

