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

### Learning Objective 1: Manipulate arrays of numbers.
# # The variable data is a list of lists. Each element 
# # in data is an x,y point on an optical absorbance spectrum.
# # The first number is the wavelength and the second number 
# # is the absorbance.

###The data:
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
print "A form that is easier to read is"
for row in data:
    print row[0], " ",row[1]

### Task 1a: Modify the array by adding (appending) a data point
# # [1000.00,20.00].
data.append([1000.00,20.00])

# # We start counting with 0 in python.  The first element is 
# # referred to by data[0] and it is [100.0, 0.0].
print "\n The first element in data is ", data[0]
print "\n The last element in data is ", data[-1]

# # Let's refer to the  elements of data as "data points"  when 
# # I say "data point" I mean a list of length 2 where the first
# # element has the meaning of wavelength and the second has the 
# # meaning of absorbance. 
# # To access the wavelength of a data point we want the first 
# # element of the data point: data[0][0]

### Task 1b. Print the wavelength of that first data point and the  absorbance  on two separate lines.

print "The wavelength of that first data point is ", data[0][0], " nm"
print "The absorbance is ", data[0][1]

### Task 2: Partition the array into a 1x1 array (list) of 
# #wavelengths and a 1x1 array (list) of absorbances.

# # Let us start by getting a list of the wavelengths.

### Learning Objective 2: Implement a loop
# # For each row in the data set, add the wavelength of that row to 
# # the list called "wavelengths"

# # Start by making an empty list of wavelengths.
wavelengths=[]
for row in data:
    tempWvlngth=row[0]
    wavelengths.append(tempWvlngth) 

# # Below, put the 'one liner' version of the same loop approach.
first_column = [ row[0] for row in data ]

# # Test with a print statement or two, note how the results here are identical.
print "\n \n The wavelengths are \n", wavelengths
print "That is the same as the variable first_column \n", first_column

# # Now  let us complete task 2 by doing the same thing for a list of absorbance values.
absorbance=[]
for row in data:
    absorbance.append(row[1]) #slightly shorter than the wavelengths loop above

# # Or you can do the one-liner form:
second_column = [ row[1] for row in data ]

# # These two results should be identical. Test this with some print statements.
print "\n \n The absorbance is \n", absorbance
print "And this should be the same as second_column \n", second_column

### Task 3. Identify the min and max absorbance and print 
# # out the wavelength and absorbance of that data point

# # The naive approach
print "naive approach to max wavelength", max(wavelengths)
print "naive approach to max absorbance", max(absorbance)
print "Unless the max absorbance corresponds to the max wavelength, then this won't give us the correct answer."


### Learning Objective 3: Implement and use a function
# # FindMax(data) takes data, list of data points, and 
# # finds the maximum of the absorbance. It returns the 
# # x and y values of the datapoint.
from ReferenceHelperFunctions import FindMax

maxWL,maxAbs=FindMax(data)
print "\n \n The maximum absorbance of this spectrum is ", maxWL , "at ", maxAbs, " nm"



### Bonus Task 4: Identify the min and max of the UV region
# # UV :10 to 380 nm

# #First Pass: Assuming my data is well behaved (that might be
# # a bad assumption),the wavelength value in my data will only be
# # increasing, that is, it won't be out of order.  
 
UV_cutoff=380 #in nm

# # What is the index of the row number that corresponds to 
# # the UV cutoff? Here's my simple algorithm design:  I will 
# # iterate through the data and determine how many rows are in the 
# # UV range. Then we use us that number of rows (i) to take 
# # a subset of the data and assign that subset to UV_subset.
# # "i" is often used as a counting variable but you can use whatever 
# # you like as long as it hasn't be used elsewhere in the code.
i=0  # # start counting at zero.
for row in data:
        if row[0]<=UV_cutoff:  # # If the value of the wvlngth of that row is smaller or equal
                               # # to the cutoff, then....do something 
            i=i+1              # # add to the indexer "i"      
            # # Once the wavelength value is bigger than the UV_cutoff, 
            # # then it will stop incrementing

print "The number of rows in the data until the UV_cutoff is ", i

# # UV_subset is the subset of data from row 0 to row i.
UV_subset=data[0:i]  
print "The UV subset of data is: ", UV_subset

# # Now we apply our function to find the max value in the new data set.
UV_max=FindMax(UV_subset)
print 'UV max ', UV_max


### Bonus Task 5: convert your approach for task 4 into a function 
# # FindEnergyBounds() in the file HelperFunctions.
# # Use that function and the data below to identify the 
# # UV :10 to 380 nm
# # Visible: 380 to 700 nm
# # IR: 700  to 10E5 nm

### Bonus Learning Objective 3a: converting a piece of 
# # code into a felxible function that can be used multiple
# # times.

from ReferenceHelperFunctions import FindEnergyBounds

# # FindEnergyBounds returns two numbers, the idexes that 
# # include min and max wavelenghts for the data set.

# # The index numbers are assigned to the return values of 
# # FindEnergyBounds.
# # 10  nm is the lower cutoff for the UV spectrum
# # 380 nm is the upper cutoff for th UV spectrum
UV_lower_i, UV_upper_i=FindEnergyBounds(10, 380, data)
print 'UV:', UV_lower_i, UV_upper_i
print FindMax(data[UV_lower_i:UV_upper_i])

# # Now I use the function again for the IR region, 700 nm to 1 mm
IR_lower_i, IR_upper_i=FindEnergyBounds(700, 10E5, data)
print 'IR:', IR_lower_i, IR_upper_i
print FindMax(data[IR_lower_i:IR_upper_i])


# # And again for the visible region.
VIS_lower_i, VIS_upper_i=FindEnergyBounds(380,700, data)
print 'VIS:', VIS_lower_i, VIS_upper_i
print FindMax(data[VIS_lower_i:VIS_upper_i])


print 'done'