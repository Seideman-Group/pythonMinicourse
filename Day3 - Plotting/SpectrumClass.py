#!/usr/bin/env python

import os
import numpy as np

# Define a custom class to organize all data
class Spectrum:
	def __init__(self,filename):
		if not os.path.isfile(filename):
			raise Exception("Spectrum object needs a valid filename")
		self.source     = filename
		info            = filename.split('_')
		self.date       = [info[0][i:i+2] for i in range(0,len(info[0]),2)]
		self.surface    = info[2]
		self.wavelength = info[4]
		self.current    = info[7]
		self.power      = info[8]
		self.time       = info[9]
		self.number     = int( info[13].split('.')[0] )
		self.data       = np.genfromtxt(self.source,usecols=(2))
