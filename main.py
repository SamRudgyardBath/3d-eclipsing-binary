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
from star import Star

def Main():
    samples = 20
    star1 = Star(np.array([0,0,0]), 2, samples)
    star2 = Star(np.array([10,0,0]), 5, samples)
    
    listStars = [star1, star2]
    ax = plt.figure().add_subplot(projection='3d')
    for i in range(0, 2):
        x, y, z = listStars[i].nodes
        position = listStars[i].position
        ax.scatter(x-position[0], y-position[1], z-position[2])
        ax.axis('equal')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot_surface(x-position[0], y-position[1], z-position[2], linewidth=0.2, antialiased=True)
    plt.show()

if __name__ == "__main__":
	Main()