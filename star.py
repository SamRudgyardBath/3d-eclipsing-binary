#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:57:54 2023

@author: sam
"""
import numpy as np
from node import Node

class Star:
    def __init__(self, pos, radius, res):
        """ 
        Star class constructor
        
        Parameters
        ----------
        pos : 3x1 array of floats
            Position of the star in cartesian coordinates: x, y, z
        radius : float
            Radius of the star
        res : float
            Resolution, determines the number of nodes that makes up the star
        """
        self.position = pos
        self.radius = radius
        
        samples = int((4 * np.pi * self.radius**2) * res / 100)
        
        nodes = []
        goldenRatio = np.pi * (np.sqrt(5) - 1) # Golden Ratio in radians
        for i in range(samples):
            y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
            radius = np.sqrt(1 - y * y)  # radius at y
    
            theta = goldenRatio * i  # golden angle increment
    
            x = np.cos(theta) * radius
            z = np.sin(theta) * radius
            
            nodes.append(Node(self.radius * x, self.radius * y, self.radius * z))
        self.nodes = np.array(nodes)
    
    def GetAllNodes(self):
        """ 
        Collects all nodes that describe the star's surface
        
        Returns
        -------
        out : array of nodes
            Array consisting of all nodes that make up the star. Nodes are with respect to the star's frame.
        """
        allNodes = []
        for node in self.nodes:
            allNodes.append(np.array([node.x, node.y, node.z]))
        return allNodes
    
    def GetAllCoords(self):
        """ 
        Organises all coordinates of nodes into separate arrays for each cartesian axes
        
        Returns
        -------
        xArray : array
            Array of all x-coordinates in the star's frame
        yArray : array
            Array of all y-coordinates in the star's frame
        zArray : array
            Array of all z-coordinates in the star's frame
        """
        xList, yList, zList = [], [], []
        for node in self.nodes:
            xList.append(node.x)
            yList.append(node.y)
            zList.append(node.z)
        xArray = np.array(xList)
        yArray = np.array(yList)
        zArray = np.array(zList)
        return xArray, yArray, zArray