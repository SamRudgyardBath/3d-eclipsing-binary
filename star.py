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
        for i in range(0, theSamples):
            y = 1 - (i / float(theSamples - 1)) * 2  # y goes from 1 to -1
            phi = i * np.pi / theSamples
            
            for j in range(0, theSamples):
                theta = 2 * j * np.pi / theSamples
            
                # Rotate so the pole of the sphere is along the x-axis
                z = self.radius * np.sin(phi) * np.cos(theta)
                y = self.radius * np.sin(phi) * np.sin(theta)
                x = self.radius * np.cos(phi)
            
                newNode = Node(x, y, z)
                nodes.append(newNode)
        self.nodes = np.array(nodes)
    
    # @property
    # def nodes(self):
    #     return self.nodes
    
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