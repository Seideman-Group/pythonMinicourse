#!/usr/bin/env python2.7

'''
This script demonstrates how to make a grid of subplots.
'''

import numpy as np
import matplotlib.pyplot as plt

def decorateAxes(ax, title):
    '''
    Decorates Axes for a plot of 2D Lorentzians
    '''

    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")


# set up data

dim = 211

x = np.linspace(0, 10*np.pi, dim)

# y data are stored in a 2D array
y = np.zeros((4, dim))
y[0,:] = np.sin(x)
y[1,:] = np.cos(x)
y[2,:] = np.tan(x)
y[3,:] = np.exp(x)

# list of titles for plots (order is left to right in each row)
titles = ["Sine", "Cosine", "TANGENT", "Exponential"]

# set up plot

fig, axes = plt.subplots(2,2) # returns a 2x2 numpy array of Axes objects

# `enumerate` lets you iterate over a list and its index.
# `zip` lets you iterate over multiple lists.
# `enumerate(zip(*)) iterates over multiple lists, plus an index
for ii, (ax, title) in enumerate(zip(axes.flat, titles)):
    ax.plot(x, y[ii,:])
    decorateAxes(ax, title)

# could also do the above manually:
    # axes[0, 0].plot(x, y[0, :])
    # decorateAxes(axes[0, 0], "Sine")
    # etc...

plt.show()