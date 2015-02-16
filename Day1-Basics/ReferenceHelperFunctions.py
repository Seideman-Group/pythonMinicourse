###############################################################################
## ReferenceHelperFunctions.py
## Author: Lindsey R. Madison
## Date: 2/10/2014
##
## Purpose: This contains functions that were inteded for use in the script
##          ReferenceSimpleDataAnalysis.py
##          ReferenceHelperFunctions can be loaded into your main script with:
##          from ReferenceHelperFunctions import NameOfFunction
###############################################################################

#Learning Objective 3: Implement and Use a function

#FindMax takes a list of lists as the input and returns two values,  max_x and max_y, such that max_y is a maximum of the data set  
#def indicates this is a function
#FindMax is the function's name
#dataList is the input variable. For this function to work as written it must be a list of lists 
def FindMax(dataList):
    #Initially set the maximum as a really small number
    max_y=-100000000000 ###point of discussion 
    #max_y=None  #Or this
    #max_y=data[0][1]  #Or this
    #For each data point in the dataList, if the second value is greater than the current max value, save that max_y and the corresponding max_x
    for row in dataList:
        if (row[1]>max_y):
            max_x=row[0]
            max_y=row[1]
    #return max_y        #Why just return one value?
    return max_x, max_y  #When we can return more than one value.
    


## Bonus Learning Objective 3a: converting a chunk of coode into a felxible function that can be used multiple times.
## FindEnergyBounds takes in the min and the max for some region of wavelengths and returns indexes of a list of lists (a.k.a. data)
## that inclusively correspond to those min/max values for the variable that corresponds to the max wavelength (which is a list of lists) 

def FindEnergyBounds(min,max,data):
    i=0
    min_i=0
    max_i=0
    for row in data:
        i=i+1
        if row[0]<=max:
            max_i=i
        if not row[0]>min:
            min_i=i
    return min_i, max_i