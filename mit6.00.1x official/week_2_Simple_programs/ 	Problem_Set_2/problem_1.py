#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:09:00 2018

@author: prime
"""

# Paste your code into this box
def ubalance(balance ,monthlyPaymentRate ,annualInterestRate, month):
    if  month <12 :
        minpay = round(balance*monthlyPaymentRate , 2)
        ub = round(balance - minpay , 2)
        interest = ub*(annualInterestRate/12.0)
        balance = round(interest + ub , 2)
        month = month+1
        return ubalance(balance, monthlyPaymentRate ,annualInterestRate,month)
    return (balance)
x = ubalance(balance, monthlyPaymentRate ,annualInterestRate, 0)
print('Remaining balance: ', x) 