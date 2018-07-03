#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 18:13:11 2018

@author: prime
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self,other):
        coordinate_same = self.x == other.x and self.y == other.y
        return coordinate_same
    def __repr__(self):  #remove this and the next line and re-run
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'