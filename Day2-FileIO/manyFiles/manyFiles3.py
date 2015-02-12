#!/usr/bin/env python

import numpy as np
import glob

##########################
### Finding many files ###
##########################

### filename parsing

# glob many files
fileList=glob.glob("/Users/benjamin/Desktop/R6G_CWUHVTERS/*.txt")


listOfData=[]
for file in fileList:
	print file.split()

# well that's useless - try a different delimeter
#	print int(terms[-1].split(".")[0])
