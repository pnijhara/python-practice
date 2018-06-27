#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:56:49 2018

@author: prime
"""
def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    def square(x):
        return x*x
    return square(pow(x,2))
        
