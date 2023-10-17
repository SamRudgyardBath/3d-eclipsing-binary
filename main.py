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
    samples = 20
    
    i = np.arange(0, samples, 1)
    y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
    radius = np.sqrt(1 - y * y)  # radius at y
    phi = np.linspace(0, np.pi, samples)
    theta = np.linspace(0, 2*np.pi, samples)
    
    phi, theta = np.meshgrid(phi, theta)
    
    # Rotate so the pole of the sphere is along the x-axis
    z = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    x = np.cos(phi)
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(x, y, z)
    ax.axis('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot_surface(x, y, z, linewidth=0.2, antialiased=True)
    plt.show()

if __name__ == "__main__":
	Main()