import numpy as np

myData=np.genfromtxt("/Users/joshuaszekely/Desktop/Codes/pythonMinicourse/day2Data/R6G_CWUHVTERS/032614_3.0A1minx2R6G_Ag111_Ag0306A_532nm_cent567_VB1V_100pA_500uW_5s_60spectra_e_at1min_1.txt")

firstColumn=myData[:,0]
thirdColumn=myData[:,2]

maxCol3=max(thirdColumn)
print maxCol3

myData[:,2]=thirdColumn/maxCol3

np.savetxt("dataBaboon.out",myData)