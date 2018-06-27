#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:01:18 2018

@author: prime
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        if char == aStr[0]:
            return True
        else:
            return False
    else:
        high = len(aStr) -1
        low = 0
        ans = len(aStr)//2
        if char == aStr[ans]:
            return True
        elif aStr[ans] > char:
            return isIn(char , aStr[:ans])
        elif aStr[ans] < char:
            return isIn(char , aStr[ans+1:])