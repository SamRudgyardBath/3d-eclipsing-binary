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
    samples = 100
    points = np.empty([samples, 3])
    phi = np.pi * (np.sqrt(5.) - 1.)  # golden angle in radians

    for i in range(0,samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = np.sqrt(1 - y * y)  # radius at y

        theta = phi * (i+1)  # golden angle increment

        x = np.cos(theta) * radius
        z = np.sin(theta) * radius

        points[i, 0], points[i, 1], points[i, 2] = x, y, z
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2])
    ax.axis('equal')
    ax.plot_surface(points[:,0], points[:,1], points[:,2], linewidth=0.2, antialiased=True)
    plt.show()

if __name__ == "__main__":
	Main()