#!/usr/bin/env python

#load data into arrays, manipulate it, and save it

########################################
### Opening and reading a known file ###
########################################

# create a file object - the thing you use to access/manipulate the file
myFile=open("biphenylP16Tau.15T0-SinglePulse-Scale1.dat",'r')

# create empty lists to store the results
xData=[]
yData=[]

# step through each line of the file in a loop, loading the text into the variable 'dataLine'
for dataLine in myFile.readlines():
	
	#split the line of text into a list of each term, by default 'split()' separates things by whitespace
	listOfTerms=dataLine.split()

	# let's do something more interesting here:
	xData.append(float(listOfTerms[0]))
	yData.append(float(listOfTerms[2])-float(listOfTerms[1]))

# close the file - don't forget the parentheses!
myFile.close()


outFile=open("data.dat",'w')

dataLength=len(xData)

for i in range(dataLength):
	outFile.write(str(xData[i])+" "+str(yData[i])+"\n")


outFile.close()

