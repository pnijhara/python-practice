#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:56:05 2018

@author: prime
"""
w = 'Wheresoever you go, go with all your heart'
k = w.lower()
l = k.split()
s = ""
for i in range(0, len(l)):
    if  l[i].isalpha():
        s = s+l[i]
        if s[0]>"g":
            print(s.capitalize())
            s = ""
        else:
            s = ""
    else:
        s = ""
        
        
        
        
        
        