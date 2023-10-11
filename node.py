#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:25:33 2023

@author: sam
"""
import numpy as np

class Node:
    def __init__(self, x, y, z):
        self.pos = np.array([x, y, z])
    @property
    def x(self):
        return self.pos[0]
    @property
    def y(self):
        return self.pos[1]
    @property
    def z(self):
        return self.pos[2]