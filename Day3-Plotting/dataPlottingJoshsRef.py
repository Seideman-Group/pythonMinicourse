"""
Objectives for Day 3 Part 1:
    - Import spectral data into python using classes
    - Make a really simple plot
    - Data manipulations
        - Smoothing
        - Baseline correction
        - Curve fitting
    - Really simple heat map

Note: Change the plotting format to SVG in preferences
Note: Also, Change the directory before using this script
"""

# Import all the modules

'''
import glob
import numpy as np
import matplotlib.pyplot as plt

from SpectrumClass import Spectrum
'''

# Import the x-axis
# Load all spectra into an array, first get all file names, then create Spectrum objects

# If on a Mac/Linux Machine, use this line:
# xData = np.genfromtxt("R6G_CWUHVTERS/032614_Ne_pt1s_20_poly3cal_1.txt",usecols=(0))
# Windows Users use this one:
# xData = np.genfromtxt("R6G_CWUHVTERS\\032614_Ne_pt1s_20_poly3cal_1.txt",usecols=(0))

'''
##Windows vs Mac difference
allFiles = glob.glob('R6G_CWUHVTERS/*cent567_VB1V*.txt')
spectra = []
for f in allFiles:
	spectra.append(Spectrum(f))
'''

# Let's sort them based on the appropriate number
# import operator as op
# spectra.sort(key=op.attrgetter('number'))


# Let's make a basic plot of one of the data sets
'''
plt.plot(xData, spectra[40].data)
plt.title("RawData")
plt.show()
'''
# Let's just work with one piece for now
'''
yData = spectra[37].data
'''
##########################################
# Noise  Correction and baseline fitting
##########################################

#import the scipy signal library
'''
import scipy.signal as ss
'''

# Median filter
'''
yData_med = ss.medfilt(yData, 5)
'''
# plt.plot(xData,yData_med)
# plt.title("Median Line Filter")
# plt.show()

# Savitsky-Golay filter
'''
yData_sav = ss.savgol_filter(yData, 5, 1)
'''
# plt.plot(xData,yData_sav)
# plt.title("Savitsky-Golay Filter")
# plt.show()

# baseline fitting
'''
baseline = ss.savgol_filter(yData,51,2)
'''
#plt.plot(xData,baseline)
#plt.title("Crude Baseline")
#plt.show()

# Now let's correct the baseline to make it a bit smoother
'''
for ii in range(51,300,30):
	baseline = ss.savgol_filter(baseline, ii, 2)
baseline = baseline - 10.0
'''

#plt.plot(xData,baseline)
#plt.title("Corrected Baseline")
#plt.show()

# Finally subtract the baseline
'''
modData = yData_sav - baseline
'''
#plt.plot(xData, modData)
#plt.title("Savitsky-Golay Filter, Baseline Subtracted")
#plt.show()

############################################################
# Peak Finding - Check scipy signal library for more options
############################################################

# finds all local max in smoothed data set
# filter out those that are too small
'''
somePeaks = ss.argrelmax(modData,order = 30)[0]
peaks = [p for p in somePeaks if modData[p] > 20.0]
'''

#plt.gcf().set_size_inches(16.0,12.0)
#plt.plot(xData, modData)
#plt.plot(xData[peaks], modData[peaks],'ro')
#plt.show()

###################################################
# Curve Fitting - one of the most requested topics
###################################################
'''
from scipy.optimize import curve_fit

def lorentzian(x,A,G,x0):
	return (A/np.pi)*(0.5*G)/( (x-x0)**2 + (0.5*G)**2)

reprodData = np.zeros(len(xData))
print "Now fitting..."
for peak in peaks:
	width = 10
	lowerInd = peak - width
	upperInd = peak + width
	xD = xData[lowerInd:upperInd]
	yD = modData[lowerInd:upperInd]
	aGuess = modData[peak]
	bGuess = xData[peak]
	cGuess = 0.5
	popt,pcov = curve_fit(lorentzian, xD, yD p0=[aGuess,bGuess,cGuess])
	print popt
	for ii in range(len(xData)):
		reprodData[ii] += lorentzian(xData[ii],popt[0],popt[1],popt[2])
'''
#plt.gcf().set_size_inches(16.0,12.0)
#plt.plot(xData, modData)
#plt.plot(xData, reprodData)
#plt.show()

#plt.gcf().set_size_inches(16.0,12.0)
#plt.plot(xData, yData)
#plt.plot(xData,reprodData+baseline,linewidth=2.0,color="black")
#plt.title("Fully fitted spectrum")
#plt.show()

# Convert to 2D array of spectra
'''
data2D  = np.zeros([len(spectra), len(yData)])
for ii in range(len(spectra)):
	data2D[ii] = spectra[ii].data

plt.pcolormesh(xData, np.arange(0,len(spectra)), data2D)
'''
#plt.axis([min(xData),max(xData),0, len(spectra)])
#plt.xlabel(r'Wavenumber / cm$^{-1}$')
#plt.ylabel("Number")
#plt.show()