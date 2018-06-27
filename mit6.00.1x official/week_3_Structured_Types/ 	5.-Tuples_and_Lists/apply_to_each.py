#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:15:57 2018

@author: prime
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def mod(a):
    return abs(a)
applyToEach(testList, mod)