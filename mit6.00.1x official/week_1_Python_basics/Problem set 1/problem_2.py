#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:49:55 2018

@author: prime
"""

i=0
count=0
while i<len(s):
    if s[i:i+3] == 'bob':
        count+=1
    i+=1
print(count)