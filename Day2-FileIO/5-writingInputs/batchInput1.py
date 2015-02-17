#!/usr/bin/env python

import numpy as np


placeHolder="$$$"

desiredValues=['50','100','250']

for val in desiredValues:
	templateFile=open("biphenyl-SP-TZdp-0.0-template.in",'r')
	outFile=open("qchemInput-"+val+".in",'w')
	
	for line in templateFile.readlines():
		if (placeHolder in line):
			outFile.write(line.replace(placeHolder,val))
		else:
			outFile.write(line)

	outFile.close()
	templateFile.close()
