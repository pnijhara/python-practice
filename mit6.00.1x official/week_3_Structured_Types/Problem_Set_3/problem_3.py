#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:22:53 2018

@author: prime
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    l1 =[]
    l = [string.ascii_lowercase]
    s = l[0]
    for i in s:
        l1.append(i)
    for word in lettersGuessed:
        l1.remove(word)
    return ' '.join(l1)
            