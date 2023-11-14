#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:21:48 2023

@author: sam
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from geometric_functions import RotateX, RotateY
from star import Star
from node import Node

fig, ax = plt.subplots()
ax.axis('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
movementStarted, movementStopped = False, False
arrowKeys = ["up", "down", "left", "right"]
dx, dy = 0, 0

def PlotStars(theListStars):
    ax.cla()
    for star in theListStars:
        x, y, z = star.GetAllCoords()
        position = star.position
        alphas = np.interp(z, [z.min(), z.max()], [0,1])
        xLab, yLab, zLab = x + position[0], y + position[1], z + position[2]
        
        for z in zLab:
            if (z < position[2]):
                i = zLab.tolist().index(z)
                xLab = np.delete(xLab, i)
                yLab = np.delete(yLab, i)
                zLab = np.delete(zLab, i)
                alphas = np.delete(alphas, i)
        
        # Scatter data points
        ax.scatter(xLab, yLab, alpha=alphas, linewidth=0.2, ls='', antialiased=True)
        ax.triplot(xLab, yLab)
        # ax.tripcolor(xLab, yLab, alphas)
    plt.draw()

samples = 10
star1 = Star(np.array([0,0,0]), 2, samples)
star2 = Star(np.array([10,0,0]), 5, samples)
listStars = [star1, star2]
PlotStars(listStars)

def OnKeyPressed(event):
    global movementStarted, movementStopped, dx, dy
    if event.key in arrowKeys:
        movementStarted = True
        if (event.key == "left"):
            dx += 1 / 40
        if (event.key == "right"):
            dx += -1 / 40
        if (event.key == "up"):
            dy += 1 / 40
        if (event.key == "down"):
            dy += -1 / 40
        for star in listStars:
            angle = np.pi * (dy)
            for i in range(0,len(star.nodes)):
                node = star.nodes[i]
                currentVector = np.array([node.x, node.y, node.z])
                newVector = RotateX(angle, currentVector)
                star.nodes[i] = Node(newVector[0], newVector[1], newVector[2])
            star.position = RotateX(angle, star.position)
            angle = np.pi * (dx)
            for i in range(0,len(star.nodes)):
                node = star.nodes[i]
                currentVector = np.array([node.x, node.y, node.z])
                newVector = RotateY(angle, currentVector)
                star.nodes[i] = Node(newVector[0], newVector[1], newVector[2])
            star.position = RotateY(angle, star.position)
        if movementStopped:
            movementStarted, movementStopped = False, False
    PlotStars(listStars)
        
def OnKeyReleased(event):
    global dx, dy
    global movementStarted, movementStopped
    if event.key in arrowKeys and movementStarted:
        movementStopped = True
        dx, dy = 0, 0

fig.canvas.mpl_connect('key_press_event', OnKeyPressed)
fig.canvas.mpl_connect('key_release_event', OnKeyReleased)