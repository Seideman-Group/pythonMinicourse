#!/usr/bin/env python2.7

'''
This script demonstrates how to make a grid of subplots.
'''

### References
# guide for laying out grids of plots
# - http://matplotlib.org/users/tight_layout_guide.html

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

# set up plot

fig, axes = plt.subplots(2,2) # returns figure and 2x2 numpy array of Axes objects

axes[0, 0].plot(x, y[0, :])
decorateAxes(axes[0, 0], "Sine")
axes[0, 1].plot(x, y[1, :])
decorateAxes(axes[0, 1], "Cosine")
axes[1, 0].plot(x, y[2, :])
decorateAxes(axes[1, 0], "TANGENT")
axes[1, 1].plot(x, y[3, :])
decorateAxes(axes[1, 1], "Exponential")

plt.title("foo")

plt.tight_layout() # prevents plot labels from overlapping

plt.show()



### Another way to do it

# list of titles for plots (order is left to right in each row)
titles = ["Sine", "Cosine", "TANGENT", "Exponential"]

fig, axes = plt.subplots(2,2)

# `enumerate` lets you iterate over a list and its index.
# `zip` lets you iterate over multiple lists.
# `enumerate(zip(*)) iterates over multiple lists, plus an index
# `axes.flat` converts the 2D numpy array to a 1D numpy array
for ii, (ax, title) in enumerate(zip(axes.flat, titles)):
    ax.plot(x, y[ii,:])
    decorateAxes(ax, title)

plt.tight_layout()

plt.show()