#!/usr/bin/env python2.7
'''
This script is an example of how to create and use a class to read in and plot
'''

#### load modules

import matplotlib.pyplot as plt
import numpy as np

#### define class

class TASpectrum:
    def __init__(self, fileName):
        '''
        Store information from TA data file.

        The data format is:
            - first row: dummy value (0.0) followed by time points in ps
            - first column: dummy value (0.0) followed by wavelengths in nm
            - other rows/columns: transient absorption values
            - metadata:
                - Date
                - Sample
                - Solvent
                - Pump energy:
                - Pump wavelength (nm):
                - Cuvette length (mm):
                - Comments: Averaging time:
                - Number of scans:
                - Time units:
                - Z axis title:
        '''

        ### set default values for metadata

        # hint: to thine own `self` be true
        # hint: match the names used in the script below, e.g. spectrum.date



        ### read in matrix of raw data

        # hint: look up genfromtxt optional parameters



        ### break apart raw data (by indexing) to get times, wavelengths and data



        ### check for bad data (NaN values)

        # hint: you can just delete the first 13 lines of data, or you can find
        # an automatic way to delete bad rows of data (harder than it sounds).
        # hint: keep the array of wavelengths with the same number of rows as
        # the array of data.



        ### read in metadata

        # hint: maybe just go line-by-line
        # hint: this string method may be useful: "--".join(["one", "II", "c"])


#### begin actual script

fileName = "ta.csv"

### read in spectrum

spectrum = TASpectrum(fileName)

### print spectrum facts

print "Sample: ", spectrum.sample # should print "Sample:  CdS blank"
print "Date: ", spectrum.date     # should print "Date:  August 21, 2013"

### plot an example time trace

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(spectrum.times, spectrum.data[30,:])
ax.set_title("TA data: " + spectrum.sample) # TODO: add date as well
ax.set_xlabel("Time") # TODO: add units to label from spectrum object
ax.set_ylabel(r'$\Delta$ A') # note the 'r' before the string
# TODO: set the x scale to be log

plt.show()



### EXTRA CREDIT ###
# Make a method for the TASpectrum class that plots a specific time trace by
# index. Example usage: spectrum.plotTrace(30)



### EXTRA EXTRA CREDIT ###
# Make a method for the TASpectrum class that plots the time trace for a
# specific wavelength. Example usage: spectrum.plotWavelength(460)
# hint:
# http://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
