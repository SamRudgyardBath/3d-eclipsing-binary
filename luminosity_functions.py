#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:43:02 2023

@author: sam
"""
import numpy as np

def GetLuminosityOfGrid(grid):
    triangles = grid.triangles
    xVals, yVals = grid.x, grid.y
    
    totalArea = 0
    for triangle in triangles:
        x1, y1 = xVals[triangle[0]], yVals[triangle[0]]
        x2, y2 = xVals[triangle[1]], yVals[triangle[1]]
        x3, y3 = xVals[triangle[2]], yVals[triangle[2]]
        area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        totalArea += area
    return totalArea