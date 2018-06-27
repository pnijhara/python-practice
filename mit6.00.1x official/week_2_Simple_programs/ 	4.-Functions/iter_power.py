#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:58:40 2018

@author: prime
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    i = base
    if exp == 0:
        base = 1
    else:
        while exp >1:
            base = base*i
            exp-=1
    
    return base