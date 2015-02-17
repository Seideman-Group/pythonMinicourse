#!/usr/bin/env python

import numpy as np
import glob

##########################
### Finding many files ###
##########################

# glob many files
fileList=glob.glob("/Users/benjamin/Desktop/R6G_CWUHVTERS/*.txt")


listOfData=[]
for file in fileList:
	listOfData.append(np.loadtxt(file))

rowsInData=len(listOfData[0])
dataSum=np.zeros(rowsInData)

for dataSet in listOfData:
	dataSum=dataSum+dataSet[:,0]

