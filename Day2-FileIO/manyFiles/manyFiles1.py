#!/usr/bin/env python

import numpy as np
import glob

##########################
### Finding many files ###
##########################

# glob many files
fileList=glob.glob("/Users/benjamin/Desktop/R6G_CWUHVTERS/*")

for file in fileList:
	print file

