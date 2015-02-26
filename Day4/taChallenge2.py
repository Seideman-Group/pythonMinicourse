#!/usr/bin/env python2.7

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit

from taClassReference import TASpectrum

### functions that you might want to play with

def r2(data, fit):
    '''
    Returns the R^2 value of a fit to data.
    '''
    mean = np.average(data)
    ss_tot = np.sum(np.power(data - mean, 2)) # total sum of squares
    ss_res = np.sum(np.power(data - fit, 2))  # residual sum of squares

    return 1.0 - ss_res/ss_tot

def decorateAxes(ax, title):
    '''
    Decorates Axes.
    '''

    ax.set_title(title)
    ax.set_xlabel("Time (ps)")
    ax.set_ylabel("Change in Absorbance")


### Set up fitting functions. `p` is an array of parameters.
# Each fit function is an instrument response function (IRF) multiplied by a
# number of exponentials.

def fit1Exp(x, *p):
    # the * before `p` means that all the arguments to this function after `x`
    # will be packed into a list (tuple). It is a way to have functions take
    # varying numbers of arguments
    return sp.special.erf(p[0]*(x - p[1]))*(p[2]*np.exp(-p[3]*(x-p[1])))

# TODO: write functions that fit with two and three exponentio


### read in csv using TASpectrum class

spectrum = TASpectrum("ta.csv")

# choose one wavelength to fit

# yData =


### Do the fits

# Initial guesses for parameters.
# IRF width, time offset, then pairs of exponential amplitudes/decay constants
guess = [0.1, 0.1, -0.015, 0.01]

# curve_fit returns optimized parameters and covariance matrix
p1, pcov1 = curve_fit(fit1Exp, spectrum.times, yData, p0=guess[0:4])
# TODO: fit to two and three exponentials


### Print table of fit parameters

# This uses a structured way to format strings. For more info, look up
# https://docs.python.org/2/library/string.html#formatexamples

params = ["IRF", "t0", "A1", "K1"]

print "Fit parameters\n"
print "{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(*params)
print "{:+.2e} {:+.2e} {:+.2e} {:+.2e}".format(*p1)
print ""


### Plot the data and the fit functions together on the same Axes
# hint: a log scale on the x axis will help you see what is going on
# hint: you can generate y data with splat (*) and the fit function a la
#   fit1Exp(spectrum.times, *p1)



### EXTRA CREDIT
# Put the above in a loop and fit every wavelength to two exponentials. Print
# the time constants K1 and K2 as a function of wavelength.

### EXTRA CREDIT
# Add a function to plot the entire absorption spectrum at a specific time point