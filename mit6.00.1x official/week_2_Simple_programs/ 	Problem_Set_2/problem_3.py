#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:10:32 2018

@author: prime
"""

# Paste your code into this box
epsilon = 0.01

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
initialBalance = balance

while abs(balance) > epsilon:
    balance = initialBalance
    lowestPayment = (upperBound - lowerBound) / 2 + lowerBound

    for month in range(12):
        balance -= lowestPayment
        balance *= 1 + monthlyInterestRate

    if balance > 0:
        lowerBound = lowestPayment
    else:
        upperBound = lowestPayment

print("Lowest Payment:", round(lowestPayment, 2))