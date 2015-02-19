#!/usr/bin/env python

import numpy as np

###################################################
### Opening, reading, manipulating, saving a known file with numpy ###
###################################################

### all sorts of reasons why you'd use the simple, old way
### maybe not really reading a vector, but a list of settings

# create a file object - the thing you use to access/manipulate the file
myData=np.loadtxt("biphenylP16Tau.15T0-SinglePulse-Scale1.dat")


# we can save just a portion of it
np.savetxt("dataSliced.out",myData[:,0:2])


#we can also edit the data
myData[:,1]=np.sqrt(myData[:,1])


newDataCol1=np.sin(data[:,1])
newDataCol2=np.sin(data[:,2])

print newDataCol2-newDataCol1

np.savetxt("dataEdited.out",myData[:,0:2])

### quiz - can you print just the first 20 rows? how about the last 20 rows?