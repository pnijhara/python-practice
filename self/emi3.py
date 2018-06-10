#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:04:34 2018

@author: prime
"""

balance = 3329
rate = 0.2
lowerbound = balance/12.0
upperbound = (balance*((1+rate/12)**12))/12.0
while True:
    minpay = (upperbound+lowerbound)/2
    lbalance = balance
    month = 0
    while month<12:
        lbalance -=minpay
        lbalance = lbalance*(1+rate/12)
        month+=1
    if lbalance<0:
        upperbound = minpay
    elif lbalance>0:
        lowerbound = minpay
    else:
        break
print(minpay)
            
        