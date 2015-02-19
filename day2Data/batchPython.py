import numpy as np

templateFile=open("sampleQChemInput.in",'r')
templateData=templateFile.readlines()
templateFile.close()

values=range(100,200,25)

for val in values:
    outFile=open("qchemInput-"+str(val)+".in",'w')
    
    for line in templateData:
        if ("$$$" in line):
            outFile.write(line.replace("$$$",str(val)))
        else:
            outFile.write(line)
    outFile.close()