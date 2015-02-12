#!/usr/bin/env python

#load data into arrays and save it

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
	xData.append(listOfTerms[0])
	yData.append(listOfTerms[1])

# close the file - don't forget the parentheses!
myFile.close()


outFile=open("data.dat",'w')

dataLength=len(xData)

for i in range(dataLength):
	outFile.write(xData[i]+" "+yData[i]+"\n")


outFile.close()


### quiz - can you save 3 columns of data?