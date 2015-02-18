#!/usr/bin/env python

import numpy as np
import glob

##########################
### Finding many files ###
##########################

# glob many files
fileList=glob.glob("/qChemOutput/*")

for file in fileList:
	print file

