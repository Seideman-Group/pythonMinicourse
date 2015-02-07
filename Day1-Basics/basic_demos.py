print "Hello Class!" #This is a print statement, it outputs to the console

"This is a string" #A string is denoted by a set of double quotes
'This is also a string' #Strings can also be defined with single quotes

print "Hello " + "Class!" # + concatanates two strings
print "Welcome "*3 # *n copies the string n times
 
"It's always fun to write python code" # If you start with a double quote, the string must end with a double quote (single quotes will be interpreted as strings
'It\'s always fun to write python code' # If you want to use the same quote marker in a string that you used to define, use\ before the quote
#List more special charecters here?

s = "I'm a string object!" # something = something else stores the something else into something
print s
print s[0] # Strings are list of charecters
print s[len(s)-1] # To get how many objects are in a list use len()
#print s[len(s)] # The last item in a list is len(list)-1 if you go above that you get an error 
print s[:5] # as lists strings can be sliced at the end,
print s[6:] # at the begining
print s[6:12] # in the middle
print s[:-1] # and defined from the end

print s[::2] # Can take any number interation
print s[::-1] #Even backwards

print s[12:4:-1] # Going backwards means if reversing order of limits

t = s[:6] + "not an int" + s[12:] #Strings are immutable so to add things on you have to create a new string
print t

i = 2
print i # To print just numbers just say print number
print str(i) + " is an int object" # To print numbers with strings, convert the numbers to strings 

print i/3 # integer divison always rounds down

f = 2. # floats are used to store non-integer values. A decimal point is used to make them
sf = 2e0 # so does the use of scientific notation

print i+f/6 # Order of operations holds, and if there is one float in the operation the answer becomes a float
print f**2 # ** is the power operator
print i**2/8 # keeps ints as ints

import math # a module of more complicated math equations
print math.sqrt(i) # For more complex operations import math module, can make ints floats

#print math.sqrt(-2) # Math can't handle complex

import cmath
print cmath.sqrt(-2) # Cmath can, j is used to denote an imaginary number

b = True # a bool object
c = False # another bool object

if(b):                  #check the first conditions, if true then do that command
    print "I am true!"
else:
    print "I am false!"

if(c):                  #check the first conditions, if false then go on
    print "I am true!"
else:                   # else ends the statement and if performed if none of the conditions are met
    print "I am false!"

if(not b):              # not returns True if condtion is False
    print "I am flase!"
else:
    print "I am true!"
    
if(not c):
    print "I am flase!"
else:
    print "I am true!"

if(b and c): # returns true if both are True
    print "We are both true!"
elif (b or c): # If first condition is not met check this one;  or returns true if at least one of the conditions is true
    print "One is true and one is flase"
else:
    print "We are both false!"

if(b):
    print "First check"
elif(not c):
    print "Second"

if(not b):
    print "First check"
elif(c):
    print "Second" # If there is no else statement and none of the conditions are true then nothing happens

