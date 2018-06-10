#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 02:30:32 2018

@author: prime
"""



def EMI_calculator(P,R , M,d):
#set rate of interest monthly
    print type(R)
    r= (R/(12.0 *100))
    print r
#chechk if monthly or quaterly installment
    if M== 'Q': 
        x=4
    else:
        x=1

    if d[-1] =='Y':
        print "duration in years"
        n = d[0:(len(d)-1)]
        print n
        m = 12 *int(n)
        print m
    elif d[-1] =='M':
        print "duration is in months"
        n = d[0:(len(d)-1)]
        print n   
        m = 1 *int(n) 
        print m

    EMI = x*(P*r*(1+r)**m)//((1+r)**m - 1)
    return EMI


print EMI_calculatr(3329,2,'Q','Y'))