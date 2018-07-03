#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:47:06 2018

@author: prime
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    letters = [letter for letter in hand.keys() for frequency in range(hand[letter])]

    # Check for validity of word in wordList
    if word not in wordList:
        return False
    # Remove letters from word one by one from list
    else:
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
    return True