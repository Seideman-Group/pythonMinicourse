#!/usr/bin/env python

import numpy as np
import glob

##########################
### Finding many files ###
##########################

def returnInt(fileName):
	terms=fileName.split("-")
	newTerms=terms[-1].split(".")
	return int(newTerms[0])

### filename parsing

# glob many files
fileList=sorted(glob.glob("data/*.out"),key=returnInt)

data=[]

for fileName in fileList:
	inFile=open(fileName,'r')
	
	for line in inFile.readlines():
		if ("Convergence criterion met" in line):
			values=line.split()
			data.append(float(values[1]))
print data


### quiz - can you normalize the data so that the lowest value is 0?
### can you save it to a file with the angle value as the first column?