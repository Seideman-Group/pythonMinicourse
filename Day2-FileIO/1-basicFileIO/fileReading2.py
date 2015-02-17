#!/usr/bin/env python

#play with the data

########################################
### Opening and reading a known file ###
########################################

# create a file object - the thing you use to access/manipulate the file
myFile=open("biphenylP16Tau.15T0-SinglePulse-Scale1.dat",'r')

# step through each line of the file in a loop, loading the text into the variable 'dataLine'
for dataLine in myFile.readlines():
	
	#split the line of text into a list of each term, by default 'split()' separates things by whitespace
	listOfTerms=dataLine.split()
	#split by commas


	# let's do something more interesting here:
	print listOfTerms[0], float(listOfTerms[2])-float(listOfTerms[1])

# close the file - don't forget the parentheses!
myFile.close()


### quiz - can you print the square root of a column?