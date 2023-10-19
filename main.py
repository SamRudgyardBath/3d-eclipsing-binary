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
ax.axis('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
movementStarted, movementStopped = False, False

def PlotStars(theListStars):
    ax.cla()
    for star in theListStars:
        x, y, z = star.GetAllCoords()
        position = star.position
        alphas = np.interp(z, [z.min(), z.max()], [0,1])
        ax.scatter(x-position[0], y-position[1], alpha=alphas, linewidth=0.2, ls='', antialiased=True)
    plt.draw()

samples = 30
star1 = Star(np.array([0,0,0]), 2, samples)
star2 = Star(np.array([10,0,0]), 5, samples)
listStars = [star1, star2]
PlotStars(listStars)

def OnMouseMove(event):
    global movementStarted, star1, movementStopped
    if event.inaxes:
        if movementStarted:
            tempPos = [event.xdata, event.ydata]
            dx = tempPos[0] - cursorInitPos[0]
            dy = tempPos[1] - cursorInitPos[1]
            angle = np.pi * (dy / fig.get_figheight())
            # TODO: Rotate all points using RotateX
            for star in listStars:
                for i in range(0,len(star.nodes)):
                    node = star.nodes[i]
                    pos = star.position
                    currentVector = np.array([node.x - pos[0], node.y - pos[1], node.z - pos[2]])
                    newVector = RotateX(angle, currentVector)
                    star.nodes[i] = Node(newVector[0], newVector[1], newVector[2])
                # TODO: Rotate all points using RotateY
                angle = np.pi * (dx / fig.get_figwidth())
                for i in range(0,len(star.nodes)):
                    node = star.nodes[i]
                    pos = star.position
                    currentVector = np.array([node.x - pos[0], node.y - pos[1], node.z - pos[2]])
                    newVector = RotateY(angle, currentVector)
                    star.nodes[i] = Node(newVector[0], newVector[1], newVector[2])
            if movementStopped:
                movementStarted, movementStopped = False, False
    PlotStars(listStars)

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