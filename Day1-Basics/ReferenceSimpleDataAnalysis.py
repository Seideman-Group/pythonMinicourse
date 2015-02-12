###############################################################################
## ReferenceSimpleDataAnalysis.py
## Author: Lindsey R. Madison
## Date: 2/10/2014
##
## Purpose: This is a reference script for the simple data analysis applications
## discussed on day 1 of the python mini course.  
## Learning Objectives: 1. Manipulate arrays of numbers  
##                      2. Implement a loop
##                      3. Implent and use a function
##
###############################################################################



##Learning Objective 1: Manipulate arrays of numbers.
#The variable data is a list of lists. Each element in data is an x,y point on an optical absorbance spectrum.
#The first number is the wavelength and the second number is the absorbance.

data=[[100.0, 0.0], [250.0, 100.0], [380.0, 190.0], [400.0, 453.3], [450.0, 124.0], [500.0, 0.0], [600.0, 40.0], [700.0, 38.0], [800.0, 0.0], [900.0, 0.0], [910.0, 0.0], [920.0, 10.0], [930.0, 20.0], [940.0, 50.0], [944.0, 100.0], [945.0, 110.0], [946.0, 100.0], [947.0, 150.0], [948.0, 120.0], [950.0, 100.0]]
print "The data is \n", data

##Task 1: Modify the array by adding (appending) a data point.
data.append([1000.00,20.00])

#We start counting with 0 in python.  The first element is referred to by data[0] and it is [100.0, 0.0].
print "\n The first element in data is ", data[0]

# Let's refer to the  elements of data as "data points"  when I say "data point" I mean a list of  
# length 2 where the first element has the meaning of wavelength and the second has the meaning 
# of absorbance. 
# To access the wavelength of a data point we want the first element of the data point: data[0][0]
print "The wavelength of that first data point is ", data[0][0], " nm"
print "The absorbance is ", data[0][1]



##Task 2: Partition the array into a 1x1 array (list) of wavelengths and a 1x1 array (list) of absorbances.

#Let us start by getting a list of the wavelengths.

#Learning Objective 2: Implement a loop
#For each row in the data set, add the wavelength of that row to the list called "wavelengths"

#Start by making an empty list of wavelengths.
wavelengths=[]
for row in data:
    tempWvlngth=row[0]
    wavelengths.append(tempWvlngth) 

#Here is a 'one liner' version of the same loop approach.
first_column = [ row[0] for row in data ]

#Note how the results here are identical.
print "\n \n The wavelengths are \n", wavelengths
print "That is the same as the variable first_column \n", first_column

#Now  let us complete task 2 by doing the same thing for a list of absorbance values.
absorbance=[]
for row in data:
    absorbance.append(row[1]) #slightly shorter than the wavelengths loop above

#Or you can do the one-liner form:
second_column = [ row[1] for row in data ]

#These two results should be identical: 
print "\n \n The absorbance is \n", absorbance
print "And this should be the same as the second column is \n", second_column


#Task 3. Identify the min and max absorbance and print out the wavelength and absorbance of that data point

#The niave 
print "naieve approach to max wavelengths", max(wavelengths)
print "naieve approach to max absorbance", max(absorbance)
print "Unless the maximum absorbance corresponds to the maximum wavelength, then this won't do what we want"


#Learning Objective 3: Implement and use a function
#FindMax(data) takes data, list of data points, and finds the maximum of the absorbance. It returns the x and y values of the datapoint.
from ReferenceHelperFunctions import FindMax

maxWL,maxAbs=FindMax(data)
print "\n \n The maximum absorbance of this spectrum is ", maxWL , "at ", maxAbs, " nm"



#Task 4: Identify the min and max of the IR region, vis region, and UV region


UV_cutoff=380 #in nm

#What is the index of the row number that corresponds to the IR cutoff?
#Simple algorithm design
i=0
for row in data:
        if row[0]<=UV_cutoff:
                i=i+1
print i

UV_subset=data[0:i]
print UV_subset

UV_max=FindMax(UV_subset)
print 'UV max ', UV_max


#Maybe I want to put that little loop in function form so that it is more felxible
#Learning Objective 3a: converting a chunk of coode into a felxible function that can be used multiple times.

from ReferenceHelperFunctions import FindEnergyBounds

UV_cutoff_lower=10 #in nm
UV_cutoff_upper=380 #in nm

UV_lower_i, UV_upper_i=FindEnergyBounds(UV_cutoff_lower, UV_cutoff_upper, data)

print 'UV:', UV_lower_i, UV_upper_i

print FindMax(data[UV_lower_i:UV_upper_i])


IR_cutoff_lower=700 #in nm
IR_cutoff_upper=10E6 #in nm

IR_lower_i, IR_upper_i=FindEnergyBounds(IR_cutoff_lower, IR_cutoff_upper, data)

print 'IR:', IR_lower_i, IR_upper_i

print FindMax(data[IR_lower_i:IR_upper_i])


VIS_cutoff_lower=380 #in nm
VIS_cutoff_upper=700 #in nm

VIS_lower_i, VIS_upper_i=FindEnergyBounds(VIS_cutoff_lower, VIS_cutoff_upper, data)

print 'VIS:', VIS_lower_i, VIS_upper_i
print FindMax(data[VIS_lower_i:VIS_upper_i])


