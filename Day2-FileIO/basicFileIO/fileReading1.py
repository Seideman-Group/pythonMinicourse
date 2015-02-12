#!/usr/bin/env python

########################################
### Opening and reading a known file ###
########################################

# create a file object - the thing you use to access/manipulate the file
myFile=open("biphenylP16Tau.15T0-SinglePulse-Scale1.dat",'r')

# step through each line of the file in a loop, loading the text into the variable 'dataLine'
for dataLine in myFile.readlines():
	
	#split the line of text into a list of each term, by default 'split()' separates things by whitespace
	listOfTerms=dataLine.split()

	#print out the first and second item on the line - remember that python lists start at 0!
	print listOfTerms[0], listOfTerms[1]

# close the file - don't forget the parentheses!
myFile.close()


### quiz - can you print the first and last column? hint: -1