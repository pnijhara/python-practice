#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:50:47 2018

@author: prime
"""

longest = ""
clongest =""

for i in range(len(s) -1):
    if(s[i] <= s[i+1] ):
       longest = longest + s[i]
       if(i==len(s) -2):
           longest = longest + s[i+1]
    else:
        longest  = longest + s[i]        
        if(len(longest) > len(clongest)):
            clongest = longest
        longest = ""        

if(len(s) == 1):
    longest = s


if(len(longest) > len(clongest)):
    print("Longest substring in alphabetical order is: " + longest)
else:
    print("Longest substring in alphabetical order is: " + clongest)