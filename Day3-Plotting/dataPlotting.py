"""
Before proceeding, change to the proper directory
Change the plotting format to SVG in preferences
"""

#!/usr/bin/env python2.7
# Change the directory before using this script

import glob, os, operator, sys
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# Let's use our custom class to store our data
from SpectrumClass import Spectrum

# If you need to change the plot size, use this
# plt.gcf().set_size_inches(8.0,6.0)

rootDir = os.getcwd() # Store current directory so we can change back later
os.chdir("R6G_CWUHVTERS")

# Import the x-axis
xData = np.genfromtxt("032614_Ne_pt1s_20_poly3cal_1.txt",usecols=(0))

# Load all spectra into an array, first get all file names, then create Spectrum objects
allFiles = glob.glob('*cent567_VB1V*.txt')
spectra  = []
for f in allFiles:
    spectra.append(Spectrum(f)) # Change name?

# Now that the data is loaded, let's move back to the root directory
os.chdir(rootDir)

# Now let's sort them based on the appropriate number
spectra.sort(key=operator.attrgetter('number'))

# Data is now fully imported!
# Let's make a basic plot of one of the data sets
plt.plot(xData, spectra[30].data)
plt.title("Raw Data")
plt.show()

yData = spectra[30].data

##########################################
# Noise  Correction and baseline fitting
##########################################

# Median Line filter
yData_med = scipy.signal.medfilt(yData, 5)
plt.plot(xData,yData_med)
plt.title("Median Line Filter")
plt.show()

# Savitsky-Golay filter
yData_sav = scipy.signal.savgol_filter(yData, 5, 1)
plt.plot(xData,yData_sav)
plt.title("Savitsky-Golay Filter")
plt.show()

# baseline fitting
baseline = scipy.signal.savgol_filter(yData, 51, 2) #This is a first approximation to the baseline

plt.plot(xData,baseline)
plt.title("Crude Baseline")
plt.show()

# Let's correct the baseline to make it a bit smoother
for ii in range(50,300,30):
    baseline = scipy.signal.savgol_filter(baseline, ii+1, 2)
baseline = baseline-np.ones(len(baseline))*10.0 #Shift it down a little

plt.plot(xData,baseline, xData, yData)
plt.title("Corrected Baseline")
plt.show()

# Finally subtract the baseline
modData = yData_sav - baseline
plt.plot(xData, modData, xData, yData-baseline)
plt.title("Savitsky-Golay Filter, Baseline Subtracted")
plt.show()


###################
# Peak Finding
###################


#peaks  = scipy.signal.find_peaks_cwt(modData, np.arange(1,5),noise_perc=10)

# finds all local max in smoothed data set
plt.gcf().set_size_inches(16.0,12.0)
somePeaks = scipy.signal.argrelmax(modData,order = 30, mode="wrap")[0]

#filter out those that are too small
peaks = [p for p in somePeaks if modData[p] > 20]

plt.plot(xData, modData)
plt.plot(xData[peaks], modData[peaks],'ro')
plt.show()

# Alternate smoothing function
#def smooth(y, box_pts):
#    box      = np.ones(box_pts)/box_pts
#    y_smooth = np.convolve(y, box, mode='same')
#    return y_smooth

#Slightly different approach
#smoothModData = smooth(modData,50)
#plt.plot(xData, modData)
#plt.plot(xData[peaks], modData[peaks],'ro')
#plt.show()

###################################################
# Curve Fitting - one of the most requested topics
###################################################

from scipy.optimize import curve_fit

#lorenzians
def gaussian(x,A,x0,s):
    return a*np.exp(-1.0*pow(x-x0,2)/(2.0*s*s))

def lorentzian(x,A,G,x0):
    return (A/np.pi)*(0.5*G)/(pow(x-x0,2) + pow(0.5*G,2))

# Make array for reproduced data
reprodData = np.zeros(len(xData))

for peak in peaks:
    width      = 10
    lowerInd   = peak-width
    upperInd   = peak+width
    xD         = xData[lowerInd:upperInd]
    yD         = modData[lowerInd:upperInd]
    aGuess     = modData[peak] # Peak Height
    bGuess     = xData[peak]   # Peak Location
    cGuess     = 0.50          # Peak width
    try:
        popt,pconv = curve_fit(lorentzian, xD, yD, p0=[aGuess,bGuess,cGuess])
    except:
        print "Error fitting peak at x =", xData[peak]
        next
    print popt
    for ii in range(len(xData)):
        reprodData[ii] += lorentzian(xData[ii],popt[0],popt[1],popt[2])

plt.gcf().set_size_inches(16.0,12.0)
plt.plot(xData, modData, xData,reprodData)
plt.show()

plt.gcf().set_size_inches(16.0,12.0)
plt.plot(xData, yData,)
plt.plot(xData,reprodData+baseline,linewidth=2.0,color="black")
plt.title("Fully fitted spectrum")
plt.show()

#Finally, a fully reconstructed spectrum

#Convert to 2D array of spectra

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
    s  = numpy.r_[x0,x,xn]
    if window == 'flat': #moving average
        w = numpy.ones(window_len,'d')
    else:
        w = eval('numpy.'+window+'(window_len)')
    y   = numpy.convolve(w/w.sum(),s,mode='valid')
    lx0 = len(x0)
    if lx0 % 2 != 0:
        lx0=lx0+1
    ly = len(y)
    y  = y[lx0/2:ly-len(xn)/2]
    return y
