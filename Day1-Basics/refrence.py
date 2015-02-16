########   STRINGS   ########
"This is a string" #A string is denoted by a set of double quotes
'This is also a string' #Strings can also be defined with single quotes

print "This is a string" # To Print strings just use print

"Hello " + "Class!" # + concatenates two strings
"Welcome "*3 # *n copies the string n times
 #print "In python line indentation is important!"

"It's always fun to write python code" # If you start with a double quote, the string must end with a double quote (single quotes will be interpreted as strings
'It\'s always fun to write python code' # If you want to use the same quote marker in a string that you used to define, use\ before the quote
#List more special characters here?
'\n' # new line
'\t' # tab
'\\' # \
'\"' # "

s = "I'm a string object!" # A string object, Strings are also lists of characters
s[0]        # Access zeroth character
len(s)      # len returns the length of the string
s[len(s)-1] # return the last character of the string

# Substring formations (A substring is some part of a parent string)
s[:5]   # returns a substring  from the beginning to 4th (5-1) character
s[6:]   # returns a substring from the 6th character to the end of the string
s[6:12] # returns a substring from the 6th character to the 11th (12-1) character
s[:-2]  # returns a substring from the beginning to the end - 2 character; ("I'm a string objec") in this case

s[::2]  # returns a substring from the beginning to the end taking every second character
s[::-1] # returns a substring from the end to the beginning taking every character in reverse order

s[12:4:-1] # returns a substring from the twelfth character to the 5th character (4+1 opposite sign as normal since step is negative) taking every character in reverse order

t = s[:6] + "not an int" + s[12:] # Strings are immutable, while you can get substrings from them you can't change a substring within its parent string; to do this make a new string


########     INTS     ########
i = 2   # An int object is a number without a decimal point

print i # To print ints just say print and then the int
print str(i) + " is an int object" # To print ints with strings, convert the ints to strings using str()
print i, "is an int object"

2/3 == 0 # Is always true; integer division always rounds down


########    FLOATS    ########
f = 2.0 # A float object

print f # To print floats just say print and then the float
print str(f) + " is a float object" # To print floats with strings, convert the floats to strings using str()
print f, "is an float object"
1.0/2.0  = 0.5 # Float division gives exact results (Within computational error)
1.0//2.0 = 0.0 # To get the integer division value use //, but the answer will still be a float
1/2.0    = 0.5 # If there are any floats in an operation the result will always be a float

########  OPERATIONS  ########
1.0 +  2.0 = 3.0 # + is the addition operator
1.0 -  2.0 = 3.0 # - is the subtraction operator
1.0 *  2.0 = 3.0 # * is the multiplication operator
1.0 /  2.0 = 3.0 # / is the division operator
2.0 ** 3.0 = 8.0 # ** is the exponentiation operator (equivalent to pow(2.0,3.0))
9.0 %  5.0 = 4.0 # % is the modulus operator (returns the remainder of division)
1.0 // 2.0 = 0.0 # // is the integer division operator

 1.0 + 2.0  / 2.0 = 2.0 # Oder of operations applies (integer division and modulus are at the same level as mult/div)
(1.0 + 2.0) / 2.0 = 1.5 # Use parenthesizes like you would for any equations to dictate which operations to do when

########  MATH/CMATH  ########
import math  # Imports the math module (Gives you access to the function in math)
import cmath # Imports the cmath module for complex versions of math
from math  import * # imports all functions from the math module into the namespace of the script (instead of math.sin(), you would use sin())
from cmath import * # imports all functions from the cmath module into the namespace of the script overwriting all previous import statments

# The from ____ import * is considered bad practice because it will overwrite conflicting function names to the last imported one. This could lead to serious typing errors

math.sin(x) # sin function argument in rad (all trig functions are the same syntax, use asin for inverse sine and sinh for hyperbolic sine)

math.log(x, [base]) # returns the log_base of x (if no base is given ln(x) is returned)

math.exp(x) # returns e^x

math.pi # returns pi
math.e  #returns e

# For a complete list (https://docs.python.org/2/library/math.html)

########   COMPLEX   ########
z = 1.1 + 1.0j # A complex object

print z # To print floats just say print and then the complex; Will always print in the form (1.1+1j)
print str(z) + " is a complex object" # To print floats with strings, convert the floats to strings using str()
print z, "is a complex object"
z - 1.0j = (1.1+0j) # If there is a complex number in the operation the answer will be a complex number

########   BOOLEANS   ########
b = True  # A bool object (True/False)
b = False # The other bool object

print b # To print bools just say print and then the bool
print str(b) + " is a bool object" # To print booleans with strings, convert the booleans to strings using str()
print b, "is a complex object"
#Boolean operators
True  and  True = True  # and returns true if both conditions are true
True  and False = False
False and True  = False
False and False = False

True  or  True  = True  # or returns true if at least one condition is true
True  or  False = True
False or  True  = True
False or  False = False

not True  = False # not returns the opposite of the condition
not False = True

A == B # Returns true if A and B are equal
A != B # Returns true if A and B are not equal
A <  B # Returns true if A is strictly less than B
A <= B # Returns true if A is less than or equal to B
A >  B # Returns true if A is strictly greater than B
A >= B # Returns true if A is greater than or equal to B

# Order of Boolean operations are and  then or
True  and False or  True  = False or  True  = True
True  and True  or  False = True  or  False = True
False and True  or  True  = False or  True  = True

False and False or  True  = False or  True  = True
False and True  or  False = False or  False = False
True  and False or  False = True  or  False = True

True  or  False and True  = True  or  False = True
True  or  True  and False = True  or  False = True
False or  True  and True  = False or  True  = True

False or  False and True  = False or  False = False
False or  True  and False = False or  False = False
True  or  False and False = True  or  False = False

# Parenthesis can be used to clear up confusion
 True or False  and False  = True or  False = True
(True or False) and False  = True and False = False

# For Comparisons ==, !=, <, >, <=, >= all have the same presidence and come before and/or
A = 1, B = 2
A < B and True = True  and True = True
A > B and True = False and True = False

# Comparison operators String together so
A < B == 2 = A < B and B == 2 = True and True = True
A < B >  A = A < B and B >  A = True and True = True


########    LISTS    ########
l = []                            # an empty list
l = [1,2,3,4,5,6,7,8,9,0]         # a list of numbers
l = ["puppy",1,2,3,4,5,6,7,8,9,0] # a list can contain multiple types, This is considered to be bad programing practice

print l # To print a list use print
print str(l) + " is a list" # To print lists with strings, convert the lists to strings using str()
print l, "is a list"

l[:5]   # returns a list slice from the beginning to 4th (5-1) element
l[6:]   # returns a list slice from the 6th element to the end of the string
l[6:12] # returns a list slice from the 6th element to the 11th (12-1) element
l[:-2]  # returns a list slice from the beginning to the end - 2 element; ["puppy",1,2,3,4,5,6,7,8]

l[1]   = 0        # replace the element in location 1 with 0
l[1:4] = [9,99,2] # replace the slice l[1:4] with the given list elements
l[1:3] = [9,99,2] # These substitutions can alter sizes of lists
l[:2]  = "puppy"  # inserting strings in this fashion results in the string being treated like a list of characters so ['p',u','p','p','y'] will be added
l[:2]  = ["puppy"]# Will replace the slice with the string "puppy"
l.append(42)      # add an element to the end of a list
l.extend([3,4,5]) # add multiple items to the end of a list
l + [3,4,5]       # concatenates to lists (same as extend)

min(l[1:]) # built in functions to find min of a function
max(l[1:]) # built in functions to find max of a function
max(l)     # returns "puppy", functions will not differentiate between types, and either error out or return a value that might be wrong

map(math.sin, l) # map will operate a function over the entire list

########    LOOPS    ########
# For loops iterate over a list and preform operations fore each member
range(n)        # a list from 0 to n-1
range(m,n)      # a list from m to n-1
range(m,n,step) # a list from m to n-1 with step size step

for i  in range(10): # Will iterate over numbers 0-9 (10-1)
    print i
for i  in range(5,10): # will iterate over 5-9 (10-1)
    print i
for i  in range(5,10,2): # will iterate over 5-9 (10-1), using a step size of 2 (5,7,9)
    print i

L = [0,1,2,3,5,6,8,89]
for i in L:   # will iterate over all elements of L
    i = i + 5 # will add 5 to all elements of L

# For loops are not smart if you have a list of mixed type it will try to do that operation on all of the elements
L[0] = "Puppy"
for i in L:   # will iterate over all elements of L including the first element "Puppy"
    i = i + 5 # will error out because you can't concatenate a string and an int
for i in L:
    L.append(i) # This will cause an infinte loop: Be careful not to add things to a list you are iterating over

#While loops run their operations while its condition is true
i = 0
while(i**2 <= 100): # Run until i**2 > 100
    i = i + 1       # add one to i each step

while(i**2 <= 100): # If the condition is already false while loops do nothing
    print "Puppy"   # This will do nothing since i is not reset and i**2 will be > 100

i = 0
while(i**2 <= 100): # If Conditions are always true then you get an infinite loop
    print "Puppy"   # This does not change i so i**2 <= 100 always

######## CONDITIONALS ########
if(True):                           # Check condition is true
    print "Do this"                 # Do this part
else:                               # If no previous conditions are true
    print "Don't do that do this"   # Then perform else

# Use elif if there are multiple cases to check you want only one to happen if true
if(False):                      # Fails check goes to next
    print "Will never happen"
elif(False):                    # Fails check goes to next
    print "Will never happen"
elif(True):                     # Passes check executes
    print "Do this"
elif(True):                     # Never seen
    print "Will never happen"
else:                           # Never seen
    print "will never happen"

# If you want to do something for multiple instances of true do this
if(True):               # Passes check
    print "Do This"     # Execute Code
else:
    print "Nope"
if(True):               # Passes check
    print "Also Do this"# Execute Code
else:                   # Note each if statement will require it's own else if you want to do something when false
    print "NOPE"
if(False):              # Fails check
    print "No"          # No else so nothing happens

# If you don't have an else and all checks are false nothing happens
if(False):                      # Fails check goes to next
    print "Will never happen"
elif(False):                    # Fails check goes to next
    print "Will never happen"
elif(False):                    # Fails check goes to next
    print "Will never happen"
elif(False):                    # Fails check goes to next
    print "Will never happen"
                                # No else exits statement without executing anything

########  FUNCTIONS  ########
# SCOPE?
# Optional Args?
# return statements?