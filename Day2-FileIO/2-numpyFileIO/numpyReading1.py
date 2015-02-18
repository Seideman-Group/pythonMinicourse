#!/usr/bin/env python

import numpy as np

###################################################
### Opening and reading a known file with numpy ###
###################################################

### all sorts of reasons why you'd use the simple, old way
### maybe not really reading a vector, but a list of settings

# create a file object - the thing you use to access/manipulate the file
myData=np.loadtxt("biphenylP16Tau.15T0-SinglePulse-Scale1.dat")

# take a look at the shape of what you loaded
print myData.shape

#numpy vector is similar to a list

# try printing, notice it is automatically truncated
print myData

# there are ways to change this behavior in numpy, but sometimes simple is best
for line in myData:
	print line
#notice how it prints as lists	


#we can also easily save the data
np.savetxt("data.out",myData)
