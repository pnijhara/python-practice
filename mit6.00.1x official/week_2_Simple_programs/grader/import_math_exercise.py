#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:06:50 2018

@author: prime
"""
# area and perimeter of polygon
import math
def polysum(n,s):
    area = (0.25*n*pow(s,2))/math.tan(math.pi/n)
    peri = pow(n*s,2)
    Sum = round(area+peri , 4)
    return Sum