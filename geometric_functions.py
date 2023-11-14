#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:15:33 2023

@author: sam
"""

"""
Geometric functions for node manipulation.
"""

import numpy as np

def RotateY(theAngle, theVector):
	rotateBy = np.array([[np.cos(theAngle), 0, np.sin(theAngle)],
				[0, 1, 0], 
				[-np.sin(theAngle), 0, np.cos(theAngle)]])
	result = np.matmul(theVector, rotateBy)
	return result

def RotateX(theAngle, theVector):
	rotateBy = np.array([[1, 0, 0],
				[0, np.cos(theAngle), -np.sin(theAngle)], 
				[0, np.sin(theAngle), np.cos(theAngle)]])
	result = np.matmul(theVector, rotateBy)
	return result