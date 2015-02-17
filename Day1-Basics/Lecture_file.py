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
A   = 1.
Gam = 1.
x0  = 2.

gam2 = Gam/2
print gam2

# Get pi for the lorentz function
from math import pi
print pi
# What point do we want to calculate?
x= 2.0
# Calculate the value of that function at that point.
lor_cen = 1/pi * A * (0.5*Gam)/((x-x0)**2 + (0.5*Gam)**2)
print "lor_cen", lor_cen
# Store values in a list
lor = []
print len(lor)
lor.append(lor_cen)
print len(lor)
print lor
x= 3.0
lor.append(1/pi * A * (0.5*Gam)/((x-x0)**2 + (0.5*Gam)**2))
print lor
# For loop examples to add multiple values to lor
for x in range(10): # x takes 0 -9
    lor.append(1/pi * A * (0.5*Gam)/((x-x0)**2 + (0.5*Gam)**2))
print lor
del(lor[0:2])
print ""
print lor

lor =[]
for x in range(-5,10): # x takes -5 -9
    lor.append(1/pi * A * (0.5*Gam)/((x-x0)**2 + (0.5*Gam)**2))
print lor
# Integration
sum_lor =0.0
for l in lor:
    sum_lor = sum_lor+l
print sum_lor
sum_lor = 0.04
if(abs(A-sum_lor) < A *0.04):
    print "Good"
elif(abs(sum_lor) == 0.04):
    print "No"
elif(abs(A-sum_lor) >= A *0.04):
    print "Bad"
else:
    print "Okay"
# Check the accuracy of the lorentz approx with conditionals

