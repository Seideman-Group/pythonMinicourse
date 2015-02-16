###############################################################################
## SimpleDataAnalysis.py
## Author: Lindsey R. Madison
## Date: 2/10/2014
##
## Purpose: This is a script for the simple data analysis applications
## discussed on day 1 of the python mini course.  
## Learning Objectives: 1. Manipulate arrays of numbers  
##                      2. Implement a loop
##                      3. Implent and use a function
##
###############################################################################

### Learning Objective 1: Manipulate arrays of numbers.
# # The variable data is a list of lists. Each element 
# # in data is an x,y point on an optical absorbance spectrum.
# # The first number is the wavelength and the second number 
# # is the absorbance.

# # The data:
#  nm     Absorb. (a.u.)
# 100.0   0.0
# 250.0   100.0
# 380.0   190.0
# 400.0   453.3
# 450.0   124.0
# 500.0   0.0
# 600.0   40.0
# 700.0   38.0
# 800.0   0.0
# 900.0   0.0
# 910.0   0.0
# 920.0   10.0
# 930.0   20.0
# 940.0   50.0
# 944.0   100.0
# 945.0   110.0
# 946.0   100.0
# 947.0   150.0
# 948.0   120.0
# 950.0   100.0

data=[[100.0, 0.0], [250.0, 100.0], [380.0, 190.0], [400.0, 453.3], [450.0, 124.0], [500.0, 0.0], [600.0, 40.0], [700.0, 38.0], [800.0, 0.0], [900.0, 0.0], [910.0, 0.0], [920.0, 10.0], [930.0, 20.0], [940.0, 50.0], [944.0, 100.0], [945.0, 110.0], [946.0, 100.0], [947.0, 150.0], [948.0, 120.0], [950.0, 100.0]]

print "The data is \n", data
print "It is easier to read in this form:"
for row in data:
    print row[0], " ",row[1]

### Task 1a: Modify the array by adding (appending) a data point
# # [1000.00,20.00].


# # We start counting with 0 in python.  The first element is 
# # referred to by data[0] and it is [100.0, 0.0].
#print "\n The first element in data is ", data[0]
#print "\n The last element in data is ", data[-1]

# # Let's refer to the  elements of data as "data points"  when 
# # I say "data point" I mean a list of length 2 where the first
# # element has the meaning of wavelength and the second has the 
# # meaning of absorbance. 
# # To access the wavelength of a data point we want the first 
# # element of the data point: data[0][0]

### Task 1b. Print the wavelength of that first data point and the
# # absorbance on two separate lines.

#print "The wavelength of that first data point is ", data[0][0], " nm"
#print "The absorbance is ", data[0][1]

### Task 2: Partition the array into a 1x1 array (list) of
# #wavelengths and a 1x1 array (list) of absorbances.

# # Let us start by getting a list of the wavelengths.

### Learning Objective 2: Implement a loop
# # For each row in the data set, add the wavelength of that row to 
# # the list called "wavelengths"

# # Start by making an empty list of wavelengths.
#wavelengths=[]




# # Below, put the 'one liner' version of the same loop approach.


# # Test with a print statement or two, note how the results here are identical.



# # Now  let us complete task 2 by doing the same thing for a list of absorbance values.
#absorbance=[]



# # Or you can do the one-liner form:


# # These two results should be identical. Test this with some print statements.



### Task 3. Identify the min and max absorbance and print 
# # out the wavelength and absorbance of that data point

# # The naive approach
#print "naive approach to max wavelength", max(wavelengths)
#print "naive approach to max absorbance", max(absorbance)
#print "Unless the max absorbance corresponds to the max wavelength, then this won't give us the correct answer."


### Learning Objective 3: Implement and use a function
# # FindMax(data) takes data, list of data points, and 
# # finds the maximum of the absorbance. It returns the 
# # x and y values of the datapoint.
#from HelperFunctions import FindMax

#maxWL,maxAbs=FindMax(data)
#print "\n \n The maximum absorbance of this spectrum is ", maxWL , "at ", maxAbs, " nm"



### Bonus Task 4: Identify the min and max of the UV region
# # UV :10 to 380 nm


# # Guiding questions:
# # 1. What are the index values the correspond to the 
# # wavelength divisions in the spectrum?
# # 2. How do you create a subset of the data?
# # Hint: subset=data[lowerbound:upperbound] 
# #       where lowerbound and upperbound are integers. 
# # 3. How can you loop through the data to find the lower 
# # and upper bound integer numbers automatically?



# # Bonus Task 5: convert your approach for task 4 into a 
# # function FindEnergyBounds() in the file HelperFunctions.
# # Use that function and the data below to identify the 
# # UV :10 to 380 nm
# # Visible: 380 to 700 nm
# # IR: 700  to 10E5 nm
### Bonus Learning Objective 3a: converting a piece of 
# # code into a flexible function that can be used multiple
# # times.
#from HelperFunctions import FindEnergyBounds
 
# # FindEnergyBounds takes in the min and the max wavelength (nm) 
# # for some region of EM radiation and returns indexes of a list of 
# # lists (a.k.a. that variable data) that inclusively corresponds
# # to the min/max wavelengths. You might use it something like:

#UV_lower_i, UV_upper_i=FindEnergyBounds(10, 380, data)
#print 'UV:', UV_lower_i, UV_upper_i

# # Then you can use those indexes to again with your previous function 
# # FindMax() to find the max absorbance in a subset of the spectrum



# # Now use the function again for the IR region, 700 nm to 1 mm


# # And again for the visible region.


print 'done'