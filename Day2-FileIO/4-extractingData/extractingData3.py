#!/usr/bin/env python

import numpy as np
import glob

##########################
### Finding many files ###


# glob many files
fileList=glob.glob("/qChemOutput/*")


for fileName in fileList:
	inFile=open(fileName,'r')
	
	for line in inFile.readlines():
		if ("Convergence criterion met" in line):
			values=line.split()
			print values[1]*10
