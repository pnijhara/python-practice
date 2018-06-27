#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:47:49 2018

@author: prime
"""

countv = 0
i=0
while i < len(s):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        countv+=1
    i+=1
print(countv)
    