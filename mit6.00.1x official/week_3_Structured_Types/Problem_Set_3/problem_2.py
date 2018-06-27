#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:20:18 2018

@author: prime
"""
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    l = []
    for letter in secretWord:
        if letter in lettersGuessed:
            l.append(letter)
        else:
            l.append('_ ')
    return ' '.join(l)
