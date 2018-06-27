#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:09:43 2018

@author: prime
"""

minpay =10
while True:
    def lowest(balance,minpay,annualInterestRate,month):
        if month <12:
            unpaidb = balance - minpay
            balance = unpaidb + annualInterestRate*unpaidb
            month+=1
            return lowest(balance,minpay,annualInterestRate,month)
        else:
            return(balance,minpay)
    tup = lowest(balance,minpay,annualInterestRate/12,month = 0)
    if tup[0]<= 0:
        break
    else:
        minpay+=10
print('Lowest Payment: ' , tup[1])