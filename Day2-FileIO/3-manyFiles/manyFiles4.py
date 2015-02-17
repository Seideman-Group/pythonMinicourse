#!/usr/bin/env python

import numpy as np
import glob

##########################
### Finding many files ###
##########################

def returnInt(fileName):
	terms=fileName.split("_")
	newTerms=terms[-1].split(".")
	return int(newTerms[0])

### filename parsing

# glob many files
fileList=sorted(glob.glob("/Users/benjamin/Desktop/R6G_CWUHVTERS/*.txt"),key=returnInt)


listOfData=[]
for file in fileList:
	terms=file.split("_")
	print int(terms[-1].split(".")[0])


### quiz - can you make it so it only loads in the first 5 files? how about even numbered files?