#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:57:54 2023

@author: sam
"""
import numpy as np

class Star:
    def __init__(self, thePos, theRadius, theSamples):
        self.position = thePos
        self.radius = theRadius
        
        i = np.arange(0, theSamples, 1)
        y = 1 - (i / float(theSamples - 1)) * 2  # y goes from 1 to -1
        radius = np.sqrt(1 - y * y)  # radius at y
        phi = np.linspace(0, np.pi, theSamples)
        theta = np.linspace(0, 2*np.pi, theSamples)
        
        phi, theta = np.meshgrid(phi, theta)
        
        # Rotate so the pole of the sphere is along the x-axis
        z = self.radius * np.sin(phi) * np.cos(theta)
        y = self.radius * np.sin(phi) * np.sin(theta)
        x = self.radius * np.cos(phi)
        
        self.nodes = np.array([x, y, z])