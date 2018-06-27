#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:52:58 2018

@author: prime
"""

high = 100
low = 0
print ("Please think of a number between 0 and 100!")
while True:
    ans = (high+low)//2
    print ("Is your secret number? " , ans)
    x = input(" Enter 'h' to indiocate the guess is too high Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    if x == 'h':
        high = ans
    elif x == 'l':
        low = ans
    elif x == 'c':
        print("Game over. Your secret number was : " , ans )
        break
    else :