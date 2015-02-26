### load modules
import matplotlib.pyplot as plt
import numpy as np

# look at taClassReference for details of importing the spectrum.
from taClassReference import TASpectrum

### begin actual script

fileName = "ta.csv"

# read in spectrum

spectrum = TASpectrum(fileName)

# print spectrum facts

print "Sample: ", spectrum.sample # should print "Sample:  CdS blank"
print "Date: ", spectrum.date     # should print "Date:  August 21, 2013"

# plot an example time trace

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(spectrum.times, spectrum.data[30,:])
ax.set_title("TA data: " + spectrum.sample) # TODO: add date as well
ax.set_xlabel("Time") # TODO: add units to label from spectrum object
ax.set_ylabel(r'$\Delta$ A') # note the 'r' before the string
# TODO: set the x scale to be log

plt.show()
