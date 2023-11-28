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
from luminosity_functions import GetLuminosity, GetVisibleNodes
from star import Star
from node import Node

fig, axs = plt.subplots(2, 1, figsize=(9,5), gridspec_kw={'height_ratios': [4, 1]})
axs[0].axis('equal')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
movementStarted, movementStopped = False, False
arrowKeys = ["up", "down", "left", "right"]
dx, dy = 0, 0

tVals = []
luminVals = []
timeStep = 0

def PlotStars(theListStars):
    global timeStep
    axs[0].cla()
    axs[1].cla()
    timeStep += 1
    if (theListStars[0].position[2] < theListStars[1].position[2]):
        frontStar = theListStars[0]
        backStar = theListStars[1]
    else:
        frontStar = theListStars[1]
        backStar = theListStars[0]
        
    frontStarVisibleNodes, backStarVisibleNodes = GetVisibleNodes(frontStar, backStar)

    if (len(frontStarVisibleNodes) != 0):
        xLab = np.array([node.x + frontStar.position[0] for node in frontStarVisibleNodes])
        yLab = np.array([node.y + frontStar.position[1] for node in frontStarVisibleNodes])
        zLab = np.array([node.z + frontStar.position[2] for node in frontStarVisibleNodes])
        alphas = np.interp(zLab, [zLab.min(), zLab.max()], [0,1])
        axs[0].scatter(xLab, yLab, alpha=alphas, linewidth=0.2, ls='', antialiased=True)
    
    if (len(backStarVisibleNodes) != 0):
        xLab = np.array([node.x + backStar.position[0] for node in backStarVisibleNodes])
        yLab = np.array([node.y + backStar.position[1] for node in backStarVisibleNodes])
        zLab = np.array([node.z + backStar.position[2]for node in backStarVisibleNodes])
        alphas = np.interp(zLab, [zLab.min(), zLab.max()], [0,1])
        axs[0].scatter(xLab, yLab, alpha=alphas, linewidth=0.2, ls='', antialiased=True)
    
    tVals.append(timeStep)
    luminosity = GetLuminosity(frontStar, backStar)
    luminVals.append(luminosity)
    axs[1].plot(tVals, luminVals)
    plt.draw()
    

resolution = 500
star1 = Star(np.array([0,0,0]), 5, 1, resolution)
star2 = Star(np.array([20,0,0]), 5, 1, resolution)
listStars = [star1, star2]
PlotStars(listStars)

def OnKeyPressed(event):
    global movementStarted, movementStopped, dx, dy
    if event.key in arrowKeys:
        movementStarted = True
        if (event.key == "left"):
            dx += 1 / 100
        if (event.key == "right"):
            dx += -1 / 100
        if (event.key == "up"):
            dy += 1 / 100
        if (event.key == "down"):
            dy += -1 / 100
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