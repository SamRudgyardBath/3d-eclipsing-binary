#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:21:48 2023

@author: sam
"""

import numpy as np
from matplotlib.backend_bases import MouseEvent
import matplotlib.pyplot as plt
from geometric_functions import RotateX, RotateY
from star import Star
from node import Node

fig, ax = plt.subplots()
# ax = plt.figure().add_subplot(projection='3d')
movementStarted, movementStopped = False, False

samples = 30
star1 = Star(np.array([0,0,0]), 2, samples)
# star2 = Star(np.array([10,0,0]), 5, samples)
# listStars = [star1, star2]
for i in range(0, 1):
    x, y, z = star1.GetAllCoords()
    position = star1.position
    ax.axis('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    zMin, zMax = z.min(), z.max()
    alphas = []
    for i in range(0, len(z)):
        alphas.append(np.interp(z[i], [zMin, zMax], [0,1]))
    alphas = np.interp(z, [zMin, zMax], [0,1])
    ax.scatter(x-position[0], y-position[1], alpha=alphas, linewidth=0.2, ls='', antialiased=True)
    
def OnMouseMove(event):
    global movementStarted, star1, movementStopped
    if event.inaxes:
        if movementStarted:
            tempPos = [event.xdata, event.ydata]
            # dx = cursorInitPos[0] - tempPos[0]
            dx = tempPos[0] - cursorInitPos[0]
            # dy = cursorInitPos[1] - tempPos[1]
            dy = tempPos[1] - cursorInitPos[1]
            angle = np.pi * (dy / fig.get_figheight())
            # TODO: Rotate all points using RotateX
            for i in range(0,len(star1.nodes)):
                node = star1.nodes[i]
                currentVector = np.array([node.x, node.y, node.z])
                newVector = RotateX(angle, currentVector)
                star1.nodes[i] = Node(newVector[0], newVector[1], newVector[2])
                # if (node != star1.nodes[i]):
                    # print("Sucessfully updated!")
                # print(newVector)
                # print(newVector)
            # TODO: Rotate all points using RotateY
            angle = np.pi * (dx / fig.get_figwidth())
            for i in range(0,len(star1.nodes)):
                node = star1.nodes[i]
                currentVector = np.array([node.x, node.y, node.z])
                newVector = RotateY(angle, currentVector)
                star1.nodes[i] = Node(newVector[0], newVector[1], newVector[2])
                # if (node != star1.nodes[i]):
                    # print("Sucessfully updated!")
                # print(newVector)
            if movementStopped:
                movementStarted, movementStopped = False, False
    x, y, z = star1.GetAllCoords()
    position = star1.position
    ax.cla()
    zMin, zMax = z.min(), z.max()
    alphas = []
    for i in range(0, len(z)):
        alphas.append(np.interp(z[i], [zMin, zMax], [0,1]))
    alphas = np.interp(z, [zMin, zMax], [0,1])
    ax.scatter(x-position[0], y-position[1], alpha=alphas, linewidth=0.2, ls='', antialiased=True)
    plt.draw()
    

def OnButtonPressed(event):
    global movementStarted
    global cursorInitPos
    if event.button == 1 and not movementStarted:
        movementStarted, cursorInitPos = True, [event.xdata, event.ydata]
        
def OnButtonReleased(event):
    global movementStarted, movementStopped
    if event.button == 1 and movementStarted:
        movementStopped = True

fig.canvas.mpl_connect('motion_notify_event', OnMouseMove)
fig.canvas.mpl_connect('button_press_event', OnButtonPressed)
fig.canvas.mpl_connect('button_release_event', OnButtonReleased)

# plt.show()