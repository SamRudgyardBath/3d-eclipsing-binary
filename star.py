#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:57:54 2023

@author: sam
"""
import numpy as np
from node import Node

class Star:
    def __init__(self, thePos, theRadius, theSamples):
        self.position = thePos
        self.radius = theRadius
        self.samples = theSamples
        
        nodes = []
        goldenRatio = np.pi * (np.sqrt(5) - 1) # Golden Ratio in radians
        for i in range(theSamples):
            y = 1 - (i / float(theSamples - 1)) * 2  # y goes from 1 to -1
            radius = np.sqrt(1 - y * y)  # radius at y
    
            theta = goldenRatio * i  # golden angle increment
    
            x = np.cos(theta) * radius
            z = np.sin(theta) * radius
            
            nodes.append(Node(self.radius * x, self.radius * y, self.radius * z))
        self.nodes = np.array(nodes)
    
    def GetAllNodes(self):
        allNodes = []
        for node in self.nodes:
            allNodes.append(np.array([node.x, node.y, node.z]))
        return allNodes
    
    def GetAllCoords(self):
        xList, yList, zList = [], [], []
        for node in self.nodes:
            xList.append(node.x)
            yList.append(node.y)
            zList.append(node.z)
        xArray = np.array(xList)
        yArray = np.array(yList)
        zArray = np.array(zList)
        return xArray, yArray, zArray