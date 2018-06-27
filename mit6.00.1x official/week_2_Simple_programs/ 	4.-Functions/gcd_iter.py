#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:00:14 2018

@author: prime
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a>b:
        i = a
    else:
        i=b
    while i>0:
        if a%i==0 and b%i==0:
            return i
        else:
            i-=1
