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
    star1 = Star(0, 2, samples)
    x, y, z = star1.nodes
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