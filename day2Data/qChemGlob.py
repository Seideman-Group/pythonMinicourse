import numpy as np
import glob

fileList=glob.glob("qChemOutput/*.out")

for fileName in fileList:
    inFile=open(fileName,'r')
    fileNameParts=fileName.split("-")
    anglePart=fileNameParts[-1]
    angle=anglePart.split(".")[0]
    print angle,
    allLines=inFile.readlines()
    for line in allLines:
        if ("Convergence criterion met" in line):
            values=line.split()
            print float(values[1])
    inFile.close()
    
### go through each file, one at a time ###

### scan each file, line by line, for "Convergence criterion met" ###

### when we find the right line, extract and print the energy ###
        
### close the file, rise and repeat ###        