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
	print file.split("_")

### now we can see what we have to work with
