print "Hello Class!"
print "Error"
"This is a string" #A string is denoted by a set of double quotes
'This is also a string' #Strings can also be defined with single quotes

print "Hello " + "Class!" # + concatenates two strings
print "Welcome "*3 # *n copies the string n times

# Goal of being able to write a Lortenzian function

# What are the parameters
x0  = 2
Gam = 1
A   = 1

# y(x) = 1/pi * A * (0.5*Gam)/((x-x0)^2 + (0.5*Gam)^2)

# int division
gam2 = Gam/2

# floats any real number
x0   = 2.0
gam2 = 1.0/2
A    = 1.0

from math import pi

x = 2.0
print 1/pi * pi * gam2/((x-x0)**2 + (gam2)**2)
print 1/pi * pi * gam2/(pow(x-x0,2) + pow(gam2,2))

def lorentz(x, A, x0, gam):
    return 1/pi * A * 0.5*gam/((x-x0)**2 + (gam*0.5)**2) # Go over this?

gam = 1.0
#for x in range(10):

print range(10)
l = range(10)
lor = []

for x in range(10):
    lor.append(lorentz(x,A,x0,gam))
print lor

print lor
for x in range(-5,10):
    lor[x] = (1/pi * A * gam2/((x-x0)**2 + (gam2)**2))
print lor
print "Debug"
print lor
for x in range(-5,10):
    lor[x] = (1/pi * A * gam2/((x-x0)**2 + (gam2)**2))
    print lor
lor = []
for x in range(-5,10):
    lor.append(lorentz(x,A,x0,gam))
#print lor
lor = []
#for x in range(-5,10,0.1):
#    lor.append(1/pi * pi * gam2/((x-x0)**2 + (gam2)**2))
#print lor

for xmult in range(-5*10, 10*10,1):
    x  = xmult/10.0
    lor.append(lorentz(x,A,x0,gam))
#print lor

s = 0.0
for l in lor:
    s = s + l * 0.1
print s
if( abs(A-s) < A * 0.01):
    print "Lorentz function Approximation is great!"
elif(abs(A-s) >  A * 0.1):
    print "Lorentz function approximation is bad, please try again"
else:
    print "Lorentz function approximation is okay, may need to be more accurate"

lor = []
s = 0
for xmult in range(-5, 10,2):
    x  = xmult
    lor.append(lorentz(x,A,x0,gam))

for l in lor:
    s = s + l 
print s
if( abs(A-s) < A * 0.05):
    print "Lorentz function Approximation is great!"
elif(abs(A-s) >  A * 0.1):
    print "Lorentz function approximation is bad, please try again"
else:
    print "Lorentz function approximation is okay, may need to be more accurate"

lor = []
s = 0
for xmult in range(-5*10, 10*10,1):
    x  = xmult/10
    lor.append(lorentz(x,A,x0,gam))

for l in lor:
    s = s + l*0.1 
print s
if( abs(A-s) < A * 0.05):
    print "Lorentz function Approximation is great!"
elif(abs(A-s) >  A * 0.1):
    print "Lorentz function approximation is bad, please try again"
else:
    print "Lorentz function approximation is okay, may need to be more accurate"

 #print "In python line indentation is important!"
#
#"It's always fun to write python code" # If you start with a double quote, the string must end with a double quote (single quotes will be interpreted as strings
#'It\'s always fun to write python code' # If you want to use the same quote marker in a string that you used to define, use\ before the quote
##List more special characters here?
#'\n' # new line
#'\t' # tab
#'\\' # \
#'\"' # "
#
#a = 75
#print a
##print a + " is an int"
#print str(a) + " is an int"
#for i in range(10):
#    print i
#for i in range(-9,10):
#    print i
## Interval?
#for i in range(3,10,3):
#    print i
## Backwards?
#for i in range(10,3,-1):
#    print i
## Non integer step
#for i in range(3,10,0.1):
#    print i
#for i in range(3*10,10*10,1):
#    print i/10
#for i in range(3*10,10*10,1):
#    print i/10.0
#
#i = 2
#f = 2.0
#i + 2
#
## Using the interactive window to do other operations
#
## Lorentz function is defined defined as 1/pi * A * 1/2Gam/((x-x0)^2 +(1/2Gam)**2)
## write a for loop that can get the values of a lorentzian centered at 1.0 and a width of 2.0 and A = pi from -2 to 3 with a numerical step of 0.01
## Print out the output in the format of x       lor value for each step
#
##What about other operations?
#import math
#math.sin(a)
#math.sqrt(a)
#math.exp(a)
#
## Complex numbers
#z = 1. + 3.5j
## Other ways of doing this (set i = 1j, or treat 1j as i
#
#
## Try math with 2.0j
## fails___
#import cmath
#cmath.sin(z)
#
##from import * feature why it's dangerous
#
## The range function takes in (starting point, end point+1, interval)
## What about iterating over structres with a non even interval?
#while(c < 100):
#    print c
#    c =c**2
#
#c = 0
#while(c < 100):
#    c =c**2
#    print c
#
#c = 0
#while(c < 100):
#    c =c**2
#    print c
#    c = c + 1
#
#c = 0
#while(c**2 < 100):
#    print c
#    c = c + 1
#
## While loops would work until the condition is no longer true: useful for when the exact iteration parameters are not known
## Let's try something harder, what about printing all integers whose sin is greater than 0
#for i in range(100):
#    if math.sin(i) > 0:
#        print i
#
#
## We just introduced a condtional, this can be used outside of for loops
#if(False):                      # Fails check goes to next
#    print "Will never happen"
#elif(False):                    # Fails check goes to next
#    print "Will never happen"
#elif(True):                     # Passes check executes
#    print "Do this"
#elif(True):                     # Never seen
#    print "Will never happen"
#else:                           # Never seen
#    print "will never happen"
#
## If you want to do something for multiple instances of true do this
#if(True):               # Passes check
#    print "Do This"     # Execute Code
#else:
#    print "Nope"
#if(True):               # Passes check
#    print "Also Do this"# Execute Code
#else:                   # Note each if statement will require it's own else if you want to do something when false
#    print "NOPE"
#if(False):              # Fails check
#    print "No"          # No else so nothing happens
#
## If you don't have an else and all checks are false nothing happens
#if(False):                      # Fails check goes to next
#    print "Will never happen"
#elif(False):                    # Fails check goes to next
#    print "Will never happen"
#elif(False):                    # Fails check goes to next
#    print "Will never happen"
#elif(False):                    # Fails check goes to next
#    print "Will never happen"
#                                # No else exits statement without executing anything
#
## Using the Lortenzian definition you did for the last and a riemann sum, calculate the area under the lorentzian using bounds where the curve is >= ____. If the area is equal to A then print :).
#
###### LISTS ######
#l = [] # an empty list
#l = [0,1,2,3,4,5,6,7,8,9] # a list
#l = range(10) # range produces a list
#print len(l) # prints the size of the list
#print l[len(l)-1] # last element of the list is len(l)-1
#print l[0] # access the first element in a list
#l[0] = 10 # change the first element in a list
#print l
#l.append(42) # add an element to the end of a list
#print l
#print l[:4] # slice up to the 4th-1 element
#print l[4:] # slice from the 4th element
#print l[3:6]# slice from 3rd element to 6th-1 element
#print l[0:4:2] # slice from 0th to 4th - 1 element including every other
#print l[::2] # print every 2nd element
#print l[::-1] #print every element backwards
#print l[5:0:-1] #print backwards means reversing the order of start and end points
#l = l + [3,8,9] # to add multiple elements to the list
#print l
#l[:3] = [9,99,2] # replace slices
#print l
#l[:4] = [9,99,2] # replacing slices in list does not need to preserve size
#print l
#print min(l) # built in functions to find min/max of a function
#print max(l)
#print map(math.sin, l) # map will operate a function over the entire list
#l[0] = "puppy" # lists do not need to store the same type of objects. While it is compilable it generally not considered to be good practice
#l[:1] = "puppy" # inserting strings into a list as a slice results in the char list to be added not the string
#print l
#l[:5] = ["puppy","zebra"] # to fix give it a list of strings
#print l
#print max(l) # max will work, but it will treat the objects equally
#del l[1] # removes an item from the list
#
#s = "I'm a string object!" # something = something else stores the something else into something
#print s
#print s[0] # Strings are list of characters
#print len(s) # To get how many objects are in a list use len()
#print s[len(s)-1]
##print s[len(s)] # The last item in a list is len(list)-1 if you go above that you get an error
#print s[:5] # as lists strings can be sliced at the end,
#print s[6:] # at the beginning
#print s[6:12] # in the middle
#print s[:-1] # and defined from the end
#
#print s[::2] # Can take any number iteration
#print s[::-1] #Even backwards
#
#print s[12:4:-1] # Going backwards means if reversing order of limits
#print l
#
#for num in l[1:]: # lists can be iterated over
#    print num*2
#for num in l:
#    print num*2 # Operations preserve type be careful not to mix types in loops
##for num in l:
##    l.append(num)
##    print l[len(l)-1]
#
#
## Problem: Use this knoweldge to write a linear regression loop for data set:____ and error of