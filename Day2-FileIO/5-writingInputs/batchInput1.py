#!/usr/bin/env python

import numpy as np


placeHolder="$$$"

desiredValues=range(100,200,25)

templateFile=open("biphenyl-SP-TZdp-0.0-template.in",'r')
templateData=templateFile.readlines()
templateFile.close()

for val in desiredValues:
	outFile=open("qchemInput-"+str(val)+".in",'w')
	
	for line in templateData:
		if (placeHolder in line):
			outFile.write(line.replace(placeHolder,str(val)))
		else:
			outFile.write(line)

	outFile.close()
