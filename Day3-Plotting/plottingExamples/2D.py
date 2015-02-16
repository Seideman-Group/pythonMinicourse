#!/usr/bin/env python2.7

import numpy as np
from numpy.random import randint as ri
import matplotlib.pyplot as plt

### References
# color maps
# - `plt.colormaps()` command gives a list
# - http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
# types of interpolation
# - http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
# annotation (arrows)
# - http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.annotate
# contour plots
# - http://matplotlib.org/examples/pylab_examples/contour_demo.html
# font properties
# - http://matplotlib.org/api/font_manager_api.html#matplotlib.font_manager.FontProperties
# nice examples
# - http://nbviewer.ipython.org/github/goFrendiAsgard/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb

### Function definitions

def Lorentz(x, w, dim):
    '''
    Returns a numpy array with a normalized Lorentzian centered on the xth point
    with width xw.
    '''
    xPts = np.linspace(0, dim - 1, dim)

    return w/(2.*np.pi*(pow(xPts - x, 2) + pow(w/2.,2)))

def Lorentz2D(x, xw, y, yw, dim):
    '''
    Returns a numpy array with a normalized 2D Lorentzian, centered at the
    (x, y) grid point, with an x/y width of xw/yw
    '''

    return np.outer(Lorentz(y, yw, dim), Lorentz(x, xw, dim))

def decorateAxes(ax):
    '''
    Decorates Axes for a plot of 2D Lorentzians
    '''

    ax.set_title("Some Lorentzians")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

def makeOutputs(fig, baseName):
    '''
    Creates .png and .pdf files
    '''

    fig.savefig(baseName + ".pdf", format="pdf")
    fig.savefig(baseName + ".png", format="png")



# Set up data

# dimension of (square) data
dim = 101

# z Data are a bunch of randomized 2D Lorentzians
zData = np.zeros((dim, dim)) # (dim, dim) is a tuple, hence the extra parens
for ii in range(0, 20):
    zData += Lorentz2D(ri(1, dim), ri(8, 12), ri(0, dim), ri(8, 12), dim)


### Plot zData

fig = plt.figure()
ax = fig.add_subplot(111)

ax.imshow(zData, origin="lower", cmap=plt.get_cmap("copper"), extent=[0, 10, 0, 10])

decorateAxes(ax)

# have to save figures first, then call plt.show()
makeOutputs(fig, "2D_imshow")

plt.show()



### Plot without interpolation

fig = plt.figure()
ax = fig.add_subplot(111)

ax.imshow(zData, interpolation="nearest", origin="lower", cmap=plt.get_cmap("copper"), extent=[0, 10, 0, 10])

decorateAxes(ax)

makeOutputs(fig, "2D_imshow_nointerpolation")

plt.show()



### Contour plot

# set up x and y data
x = np.linspace(0, 10, dim)
y = np.linspace(0, 10, dim)
xData, yData = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111)

levels = np.linspace(0, 0.01, 11)

# plot both the 2D data and the contours
ax.imshow(zData, origin="lower", cmap=plt.get_cmap("Reds"), extent=[0, 10, 0, 10])
C = ax.contour(xData, yData, zData, levels, cmap=plt.get_cmap("Blues"), linewidths=(2))
fig.colorbar(C)

# find highest peak and coordinates
coord = np.unravel_index(zData.argmax(), zData.shape) # returns (y index, x index)
xp, yp = x[coord[1]], y[coord[0]]

# save some space
from matplotlib.font_manager import FontProperties as fp

ax.annotate("Best Peak", xy=(xp, yp),  xycoords="data",
            xytext=(-70, -50), textcoords="offset points",
            arrowprops=dict(arrowstyle="->"),
            fontproperties=fp(size=16, weight="bold")
            )

decorateAxes(ax)
makeOutputs(fig, "2D_contour")

plt.show()