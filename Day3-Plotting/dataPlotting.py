#!/usr/bin/env python2.7

import glob, os, operator
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# Let's use our custom class to store our data
from SpectrumClass import Spectrum

# Change to the proper directory
os.chdir("R6G_CWUHVTERS")

# Import the x-axis
xData = np.genfromtxt("032614_Ne_pt1s_20_poly3cal_1.txt",usecols=(0))

# Load all spectra into an array, first get all file names, then create Spectrum objects
allFiles = glob.glob('*cent567_VB1V*.txt')
spectra  = []
for f in allFiles:
    spectra.append(Spectrum(f))

# Now let's sort them based on the appropriate number
spectra.sort(key=operator.attrgetter('number'))

# Data is now fully imported!
# Let's make a basic plot of one of the data sets

plt.plot(xData, spectra[30].data)
plt.title("Raw Data")
plt.show()

yData = spectra[30].data

######################
# Noise  Correction
######################

# Median Line filter

yData_corr = scipy.signal.medfilt(yData, 5)
plt.plot(xData,yData_corr)
plt.title("Median Line Filter")

# Savgol-Golay filter

yData_sav = scipy.signal.savgol_filter(yData, 5, 1)
plt.plot(xData,yData_sav)
plt.title("Savitsky-Golay Filter")
plt.show()

# baseline subtraction

median   = np.median(yData)
baseline = scipy.signal.savgol_filter(yData, 299, 2) #This is a first approximation to the baseline

diff  = np.abs(yData_sav - baseline)
width = max(diff) - min(diff)
bad   = diff/width > 0.4

yData_base      = yData_sav.copy()
yData_base[bad] = baseline[bad]

# baseline = scipy.signal.savgol_filter(yData_base, 299, 2) #Correct Baseline

modData = yData_sav - baseline
plt.plot(xData, modData, xData, yData-baseline)
plt.title("Savitsky-Golay Filter, Baseline Subtracted")
plt.show()

###################
# Peak Finding
###################

def test(xD,yD,num,num2,num3=10.0, num4=5, num5=4):
    # plt.plot(xD,yD)
    somePeaks  = scipy.signal.find_peaks_cwt(yD, np.arange(num,num2),noise_perc=num3)
    otherPeaks = scipy.signal.argrelmax(yD,order = num4, mode="wrap")[0]
    peaks = [p for p in somePeaks if set([]) != ( set(otherPeaks) & set(range(p-num5,p+num5)) ) ]
    # plt.plot(xD[peaks],yD[peaks],'ro',markersize=10)
    # plt.plot(xD[list(somePeaks)],yD[list(somePeaks)],'bs')
    # plt.plot(xD[list(otherPeaks)],yD[list(otherPeaks)],'g^')
    # plt.show()
    return peaks

#Still not the best for getting peaks
peaks = test(xData, modData, 5, 10, 10, 10, 5)
plt.plot(xData, modData)
plt.plot(xData[peaks], modData[peaks],'ro')
plt.show()

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

#Slightly different approach
smoothModData = smooth(modData,50)
peaks = test(xData, smoothModData, 5, 10, 10, 10, 5)
plt.plot(xData, modData)
plt.plot(xData[peaks], modData[peaks],'ro')
plt.show()

#################################
# Curve Fitting
#################################

from scipy.optimize import curve_fit

def gaussian(x,a,b,c):
    return a*np.exp(-1.0*pow(x-b,2)/(2.0*c*c))

peaks = [p for p in peaks if (p > 10 and p < len(xData)-10)]

reprodData = np.zeros(len(xData))

for peak in peaks:
    width = 10
    lowerInd = peak-width
    upperInd = peak+width
    xD = xData[lowerInd:upperInd]
    yD = modData[lowerInd:upperInd]
    aGuess = modData[peak]
    bGuess = xData[peak]
    cGuess = 0.5
    popt,pconv = curve_fit(gaussian, xD, yD, p0=[aGuess,bGuess,cGuess])
    print popt
    for ii in range(len(xData)):
        reprodData[ii] += gaussian(xData[ii],popt[0],popt[1],popt[2])

plt.plot(xData, modData, xData,reprodData)
plt.show()



#####################
# A gift from Marty
#####################

def smooth(x,window_len=10,window='hanning'):
    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."
    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."
    if window_len<3:
        return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
    x0 = x[window_len-1:0:-1]
    xn = x[-1:-window_len:-1]
    s = numpy.r_[x0,x,xn]
    if window == 'flat': #moving average
        w = numpy.ones(window_len,'d')
    else:
        w = eval('numpy.'+window+'(window_len)')
    y = numpy.convolve(w/w.sum(),s,mode='valid')
    lx0 = len(x0)
    if lx0 % 2 != 0:
        lx0=lx0+1
    ly = len(y)
    y  = y[lx0/2:ly-len(xn)/2]
    return y
