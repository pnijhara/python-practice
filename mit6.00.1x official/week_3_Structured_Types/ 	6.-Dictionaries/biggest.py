#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:18:14 2018

@author: prime
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = 0 
    ans = None
    for key in aDict.keys():
        if len(aDict[key]) >= biggest:
            ans = key
            biggest = len(aDict[key])
    return ans