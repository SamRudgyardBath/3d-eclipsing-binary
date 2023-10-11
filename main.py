#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:21:48 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt
from geometric_functions import RotateY, RotateY
from node import Node

def Main():
    samples = 1000
    points = np.empty([3, samples])
    phi = np.pi * (np.sqrt(5.) - 1.)  # golden angle in radians

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = np.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = np.cos(theta) * radius
        z = np.sin(theta) * radius

        points[0, i], points[1, i], points[2, i] = x, y, z
    
    plt.figure().add_subplot(111, projection='3d').scatter(points[0], points[1], points[2])
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
	Main()