#!/usr/bin/env python2.7

import numpy as np
from numpy.random import randint as ri
import matplotlib.pyplot as plt

#### References ################################################################

# color maps: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps

# pyplot documentation: http://matplotlib.org/api/pyplot_api.html

# nice examples: http://nbviewer.ipython.org/github/goFrendiAsgard/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
# http://matplotlib.org/gallery.html

#### Function definitions ######################################################
import os
print(os.getcwd())

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

#### Set up data ###############################################################

# (square) dimension of data
dim = 101

# z Data are a bunch of randomized 2D Lorentzians
zData = np.zeros((dim, dim)) # (dim, dim) is a tuple, hence the extra parens
for ii in range(0, 20):
    zData += Lorentz2D(ri(0, dim), ri(3, 6), ri(0, dim), ri(3, 6), dim)

#### plot zData ################################################################

plt.imshow(zData, origin="lower", cmap=plt.get_cmap("copper"), extent=[0, 10, 0, 10])

# have to save figures first, then call plt.show()
plt.savefig('2D_imshow.pdf', format='pdf')
plt.savefig('2D_imshow.png', format='png')

plt.show()

## plot zData with xData and yData #############################################
# x and y points need to be matrices
### Things to include
# imshow
# matshow
# plotting data types
  # just a matrix (e.g. image)
  # matrix with known x and y ranges
  # 3D data
# 2D plotting functions
  # imshow/matshow
  # pgrid
# color maps and link to list
# contour plot