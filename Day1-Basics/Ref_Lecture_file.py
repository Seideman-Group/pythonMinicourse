# Basics of Strings
print "Hello Class!"
print "Error"
"This is a string" #A string is denoted by a set of double quotes
'This is also a string' #Strings can also be defined with single quotes

print "Hello " + "Class!" # + concatenates two strings
print "Welcome "*3 # *n copies the string n times

# Goal of being able to write a Lortenzian function

# y(x) = 1/pi * A * (0.5*Gam)/((x-x0)^2 + (0.5*Gam)^2)

# What are the parameters
x0  = 2 # set the center to 2
Gam = 1 # set the width to 1
A   = 1 # set A to 1

# int division
gam2 = Gam/2
print gam2 # Will = 0 since int division always rounds down

# floats any real number
x0   = 2.0
Gam  = 1.0
gam2 = Gam/2
A    = 1.0

# Get pi for the lorentz function
from math import pi # from (library) import (member)
print pi # pi is now defined within the scope of the script

# What point do we want to calculate?
x = 2.0

# Calculate the value of that function at that point.
lor_cen = 1/pi * pi * gam2/((x-x0)^2 + (gam2)^2) # ^ is not exponentiation

lor_cen = 1/pi * pi * gam2/((x-x0)**2 + (gam2)**2) # use **

# Store values in a list
lor = [] # An empty list to store values in
# Add the first value
lor.append(lor_cen)
# set x
x = 3
# Add the next value
lor.append(1/pi * pi * gam2/((x-x0)**2 + (gam2)**2))

# IDE range example
print range(10)      # 0 to 9
print range(-1,10)   # -1 to 9
print range(-1,10,2) # -1 to 9 taking every other number
l =range(10)         # Can store the output of range into a list

# For loop examples to add multiple values to lor
for x in range(10): # for (iterator variable will over ride previous definitions) in (list itertating over): Colon tells python to expect a new indentation block
    value =  1/pi * pi * gam2/((x-x0)**2 + (gam2)**2)
    lor.append(value)
print lor
del(lor[0:2]) # remove the first 2 values in a list similar to how range works with start/end points
lor = []      # clear out lor
for x in range(-5,10):
    value =  1/pi * pi * gam2/((x-x0)**2 + (gam2)**2)
    lor.append(value)
print lor

# Integration
sum_lor = 0.0
for l in lor: # iterate over all values in lor
    sum_lor = sum_lor + l # add each value of list lor to sum_lor
print sum_lor

# Check the accuracy of the lorentz approx with conditionals
if (abs(A-sum_lor) < A * 0.04):   # if(condtion is true)
    print "Good"                  # execute
elif (abs(A-sum_lor) >= A * 0.5): # if first condition is false, and this is true
    print "Bad"                   # excuete
elif (abs(A-sum_lor) > A * 0.4):  # if previouse conditions are false and this is true
    print "BAD"                   # execute
else:                             # If all other conditions are false
    print "Okay"                  # execute
