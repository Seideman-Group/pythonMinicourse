###############################################################################
## HelperFunctions.py
## Author: Lindsey R. Madison
## Date: 2/10/2014
##
## Purpose: This contains functions that were inteded for use in the script
##          SimpleDataAnalysis.py
##          HelperFunctions can be loaded into your main script with:
##          from HelperFunctions import NameOfFunction
###############################################################################

#Learning Objective 3: Implement and Use a function

#FindMax takes a list of lists as the input and returns two values,  max_x and max_y, such that max_y is a maximum of the data set  
#def indicates this is a function
#FindMax is the function's name
#dataList is the input variable. For this function to work as written it must be a list of lists 
def FindMax(dataList):
    #For each data point in the dataList, 
    #if the second value (the absorbance) is greater than the current max value, 
    #then save that as max_y and the corresponding max_x
   
    
    
    
    
                 
    
    return ReturnValues  #Return variables
    


## Bonus Learning Objective 3a: converting a chunk of coode into a felxible function that can be used multiple times.
## FindEnergyBounds takes in the min and the max for some region of wavelengths and returns indexes of a list of lists (a.k.a. data)
## that inclusively correspond to those min/max values for the variable that corresponds to the max wavelength (which is a list of lists) 

def FindEnergyBounds(min,max,data):
#Here is one approach you could try:
#For each row in the data, 
#if the first value in that row (the wavelength) is less than my max wavelength,
#then my max wavelength must be bigger. Thus I'll increment a counter

#if the first value in that row (the wavelength) is NOT larger than my min wavelength,(it is smaller)
#then my minimum index must be bigger. Thus, I'll increment a different counter

#This approach is just one solution of many. If your return values are correct and you use a different algorithm, that is perfectly fine!

    return ReturnValues