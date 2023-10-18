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
import math

def RotateY(theAngle, theVector):
	rotateBy = np.array([[math.cos(theAngle), 0, math.sin(theAngle)],
				[0, 1, 0], 
				[-math.sin(theAngle), 0, math.cos(theAngle)]])
	result = np.matmul(theVector, rotateBy)
	return result

def RotateX(theAngle, theVector):
	rotateBy = np.array([[1, 0, 0],
				[0, math.cos(theAngle), -math.sin(theAngle)], 
				[0, math.sin(theAngle), math.cos(theAngle)]])
	result = np.matmul(theVector, rotateBy)
	return result