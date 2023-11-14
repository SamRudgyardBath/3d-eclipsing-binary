#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:43:02 2023

@author: sam
"""
import numpy as np

def GetLuminosityOfGrid(grid):
    """ 
    Calculates the luminosity of a grid object by iterating through all triangles and summing the areas
    
    Parameters
    ----------
    grid : matplotlib.tri.Triangulation
        The grid containing all triangles that make up the mesh
    
    Returns
    -------
    out : float
        Luminosity of the entire grid
    """
    triangles = grid.triangles
    xVals, yVals = grid.x, grid.y
    
    totalArea = 0
    for triangle in triangles:
        x1, y1 = xVals[triangle[0]], yVals[triangle[0]]
        x2, y2 = xVals[triangle[1]], yVals[triangle[1]]
        x3, y3 = xVals[triangle[2]], yVals[triangle[2]]
        # Calculate the area using half the determinant method:
        #             | x1 y1 1 |
        # Area = .5 * | x2 y2 1 |
        #             | x3 y3 1 |
        area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        totalArea += area
    return totalArea