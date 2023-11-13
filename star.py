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
        theta = np.linspace(0, 2 * np.pi, theSamples)
        phi = np.linspace(0, np.pi, theSamples)
        [THETA, PHI] = np.meshgrid(theta, phi)
        # sphere parametrization
        Z = self.radius * np.cos(THETA) * np.sin(PHI)
        Y = self.radius * np.sin(THETA) * np.sin(PHI)
        X = self.radius * np.cos(PHI)
        
        for i in range(0, theSamples):
            for j in range(0, theSamples):
                xVal = X[i, j]
                yVal = Y[i, j]
                zVal = Z[i, j]
                nodes.append(Node(xVal, yVal, zVal))
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
    
