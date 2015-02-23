#!/usr/bin/env python2.7

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit

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


### read in csv

# `invalid_raise=False`: ignore any lines that don't match the pattern
data = np.genfromtxt("ta.csv", delimiter=",", invalid_raise=False)
# could also manually specify which lines to ignore:
# data = np.genfromtxt("foo.csv", delimiter=",", skip_header=1, skip_footer=11)
# but less general

times = data[0,1:] # first row is time points, first one is a dummy value
wavelengths = data[13:,0] # first column is wavelengths, first 13 rows have junk (NaN)
data = data[13:,1:]

# take an average of several time traces around the wavelength of interest
avgData = np.sum(data[27:33,:], axis=0)
avgData -= avgData[0] # approximate baseline as first value


### Set up fitting functions. `p` is an array of parameters.
# Each fit function is an instrument response function (IRF) multiplied by a
# number of exponentials.

def fit1Exp(x, *p):
    # the * before `p` means that all the arguments to this function after `x`
    # will be packed into a list (tuple). It is a way to have functions take
    # varying numbers of arguments
    return sp.special.erf(p[0]*(x - p[1]))*(p[2]*np.exp(-p[3]*(x-p[1])))

def fit2Exp(x, *p):
    return sp.special.erf(p[0]*(x - p[1]))*(p[2]*np.exp(-p[3]*(x-p[1])) + p[4]*np.exp(-p[5]*(x-p[1])))

def fit3Exp(x, *p):
    return sp.special.erf(p[0]*(x - p[1]))*(p[2]*np.exp(-p[3]*(x-p[1])) + p[4]*np.exp(-p[5]*(x-p[1])) + p[6]*np.exp(-p[7]*(x-p[1])))

def fit4Exp(x, *p):
    return sp.special.erf(p[0]*(x - p[1]))*(p[2]*np.exp(-p[3]*(x-p[1])) + p[4]*np.exp(-p[5]*(x-p[1])) + p[6]*np.exp(-p[7]*(x-p[1])) + p[8]*np.exp(p[9]*(x-p[1])))


### do the fits

# Initial guesses for parameters.
# IRF width, time offset, then pairs of exponential amplitudes/decay constants
guess = [0.1, 0.1, -0.015, 0.01, -0.01, 0.001, -0.01, 0.0002, -0.01, 0.0001]

# curve_fit returns optimized parameters and covariance matrix
p1, pcov1 = curve_fit(fit1Exp, times, avgData, p0=guess[0:4])
p2, pcov2 = curve_fit(fit2Exp, times, avgData, p0=guess[0:6])
p3, pcov3 = curve_fit(fit3Exp, times, avgData, p0=guess[0:8])
p4, pcov4 = curve_fit(fit4Exp, times, avgData, p0=guess[0:10])


### print R^2

# Here the `*` before `pX` means to take the list `pX` and expand it as
# separate arguments to the `fitXExp` function
print "R^2 with 1 exponential: ", r2(avgData, fit1Exp(times, *p1))
print "R^2 with 2 exponential: ", r2(avgData, fit2Exp(times, *p2))
print "R^2 with 3 exponential: ", r2(avgData, fit3Exp(times, *p3))
print "R^2 with 4 exponential: ", r2(avgData, fit4Exp(times, *p4))


### plot the fit results together

allData = np.zeros((4, len(times)))
allData[0,:] = fit1Exp(times, *p1)
allData[1,:] = fit2Exp(times, *p2)
allData[2,:] = fit3Exp(times, *p3)
allData[3,:] = fit4Exp(times, *p4)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(times, avgData, 'r.')
ax.plot(times, allData[0,:])
ax.plot(times, allData[1,:])
ax.plot(times, allData[2,:])
ax.plot(times, allData[3,:])

ax.set_xscale("log")

plt.show()


### Print table of fit parameters

# This uses a structured way to format strings. Look up
# https://docs.python.org/2/library/string.html#formatexamples

params = ["IRF", "t0", "A1", "K1", "A2", "K2", "A3", "K3", "A4", "K4"]

print "Fit parameters\n"
print "{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(*params)
print "{:+.2e} {:+.2e} {:+.2e} {:+.2e}".format(*p1[0:4])
print "{:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e}".format(*p2[0:6])
print "{:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e}".format(*p3[0:8])
print "{:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e} {:+.2e}".format(*p4[0:10])
print ""


### plot the fit results individually
# see `subplots.py` for reference

fig, axes = plt.subplots(2, 2, figsize=(12,8))

for ii, ax in enumerate(axes.flat):
    ax.plot(times, avgData, 'r.')
    ax.plot(times, allData[ii,:])
    ax.set_xscale("log")
    decorateAxes(ax, str(ii+1) + " Exponential")

plt.tight_layout()

plt.show()
