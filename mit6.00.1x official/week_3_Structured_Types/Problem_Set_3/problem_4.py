#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:23:49 2018

@author: prime
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    allowedGuesses = 8
    lettersGuessed = ''
        
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')
    
    while allowedGuesses > 0:
        print('You have', allowedGuesses, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        inputLetter = input('Please guess a letter: ')
        inputLetter = inputLetter.lower()
        
        if inputLetter in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        elif inputLetter not in secretWord:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            lettersGuessed += inputLetter
            allowedGuesses -= 1
        else:
            lettersGuessed += inputLetter
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            if isWordGuessed(secretWord, lettersGuessed):
                print('Congratulations, you won!')
                break
        
    if allowedGuesses == 0:    
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
    
