#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:55:39 2018

@author: prime
"""
balance = 3329
rate = 0.2
lowerbound = balance/12.0
upperbound = (balance*((1+rate/12)**12))/12.0

while True:
    minpay = (upperbound - lowerbound) / 2 + lowerbound
    def lowest(balance,minpay,rate,month):
        if month <12:
            unpaidb = balance - minpay
            balance = unpaidb + rate*unpaidb
            month+=1
            return lowest(balance,minpay,rate,month)
        else:
            return(balance,minpay)
    tup = lowest(balance,minpay,rate/12.0,month = 0)
    if tup[0] > 0 :
        lowerbound = minpay
    elif tup[0] < 0 :
        upperbound = minpay
    elif tup[0] == 0:
        break
print(tup[1])
    
