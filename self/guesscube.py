#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:52:36 2018

@author: prime
"""

cube = float(input("enter number : "))
error = 0.0001
guess = 0.0
increament = 0.00001
num_guess = 0
while abs(guess**3 - cube) >= error:
    guess += increament
    num_guess+=1
print('number of guesses ' , num_guess)
print(guess, " is the closest cube root of ", cube )
    
    