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

### numpy loadtxt not very useful here

### filename parsing

# glob many files
fileList=sorted(glob.glob("data/*.out"),key=returnInt)

print fileList

