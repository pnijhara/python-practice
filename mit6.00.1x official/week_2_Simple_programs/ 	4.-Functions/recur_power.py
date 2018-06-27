#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:59:41 2018

@author: prime
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0 :
        return 1
    else:
        if exp == 1:
            return base
        else :
            return base*recurPower(base,exp-1)