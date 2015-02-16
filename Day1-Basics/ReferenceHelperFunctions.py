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
    return max_x, max_y  #When we can return more than one.
    


### Bonus Learning Objective 3a: converting a piece of 
# # code into a felxible function that can be used multiple
# # times.

# # FindEnergyBounds takes in the min and the max wavelength (nm) 
# # for some region of EM radiation and returns indexes of a list of 
# # lists (a.k.a. that variable data) that inclusively corresponds
# # to the min/max wavelengths. 

def FindEnergyBounds(min_wl,max_wl,data):
    i=0   #index "i" will just be counting my rows in my data.
    min_i=0   #min_i will be the index of the lowest wavelength in the range.
    max_i=0   #max_i will be the index of the highest wavelength in the range.
    for row in data:   #loop through the data
        i=i+1         # increment the indexer as we go.
        if row[0]<=max_wl:  #if the wvlngth of our current row is < or = the max_wl...
            max_i=i         #...then max_i can be assigned to our current index value.
        if not row[0]>min_wl:  #if the wvlngth of our current row is not > min_wl...
                                # (aside: logic-wise, this if statement is very similar 
                                # to the first if statement.)
            min_i=i         #...then min_i is assigned to our current index value.
    return min_i, max_i