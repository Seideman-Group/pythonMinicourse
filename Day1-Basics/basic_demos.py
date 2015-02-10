print "Hello Class!" #This is a print statement, it outputs to the console

###### STRINGS ######
"This is a string" #A string is denoted by a set of double quotes
'This is also a string' #Strings can also be defined with single quotes

print "Hello " + "Class!" # + concatenates two strings
print "Welcome "*3 # *n copies the string n times
 print "In python line indentation is important!"

"It's always fun to write python code" # If you start with a double quote, the string must end with a double quote (single quotes will be interpreted as strings
'It\'s always fun to write python code' # If you want to use the same quote marker in a string that you used to define, use\ before the quote
#List more special characters here?
'\n' # new line
'\t' # tab
'\\' # \
'\"' # "

s = "I'm a string object!" # something = something else stores the something else into something
print s
print s[0] # Strings are list of characters
print len(s) # To get how many objects are in a list use len()
print s[len(s)-1]
#print s[len(s)] # The last item in a list is len(list)-1 if you go above that you get an error
print s[:5] # as lists strings can be sliced at the end,
print s[6:] # at the beginning
print s[6:12] # in the middle
print s[:-1] # and defined from the end

print s[::2] # Can take any number iteration
print s[::-1] #Even backwards

print s[12:4:-1] # Going backwards means if reversing order of limits

t = s[:6] + "not an int" + s[12:] #Strings are immutable so to change the characters you need to make a new string
print t

###### NUMBER TYPES ######
i = 2
print i # To print just numbers just say print number
print str(i) + " is an int object" # To print numbers with strings, convert the numbers to strings

print i/3 # integer division always rounds down

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

###### CONDITIONALS ######

b = True # a bool object
c = False # another bool object

if(b):                  #check the first conditions, if true then do that command
    print "I am true!"
else:
    print "I am false!"

if(c):                  #check the first conditions, if false then go on
    print "I am true!"
else:                   # else ends the statement and is performed if none of the conditions are met
    print "I am false!"

if(not b):              # not returns True if condition is False
    print "I am false!"
else:
    print "I am true!"

if(not c):
    print "I am false!"
else:
    print "I am true!"

if(b and c): # returns true if both are True
    print "We are both true!"
elif (b or c): # If first condition is not met check this one;  or returns true if at least one of the conditions is true
    print "One is true and one is false"
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

###### LISTS ######
l = [] # an empty list
l = [1,2,3,4,5,6,7,8,9,0] # a list
print l[0] # access the first element in a list
l[0] = 10 # change the first element in a list -> unlike strings normal lists are mutable
print l
l[0] = "puppy" # lists do not need to store the same type of objects. While it is compilable it generally not considered to be good practice
l.append(42) # add an element to the end of a list
print l
l = l + [3,8,9] # to add multiple elements to the list
print l
l[:3] = [9,99,2] # replace elements
print l
l[:4] = [9,99,2] # replacing elements in list does not need to preserve size
print l
print min(l) # built in functions to find min/max of a function
print max(l)
print map(math.sin, l) # map will operate a function over the entire list

l[:1] = "puppy" # inserting strings into a list as a slice results in the char list to be added not the string
print l
l[:5] = ["puppy"] # to fix give it a list of strings
print l
print max(l) # max finds the max value even if not the same type
del l[1] # removes an item from the list
print l

for num in l[1:]: # lists can be iterated over
    print num*2
for num in l:
    print num*2 # Operations preserve type be careful not to mix types in loops

#for num in l:
#    l.append("Time for Infinite loop") # be careful to not to append items to lists you are iterating over
#    print l[len(l)-1]

for i  in range(10): # use range to create a list of numbers to iterate over (start at 0 and go until 10-1)
    print i

for i  in range(5,10): # Sets beginning and end points (start at 5 and go until 10-1)
    print i

for i  in range(5,10,2): # alters how big iteration step is, (start at 5 and go until 10-1, taking every second number)
    print i
#
#p = math.pi
#for i in range(p): # can only use ints for range
#    print i

i = 0
while(i < len(l)): #while loops iterate until a conditional statement is no longer true
    print l[i]
    i = i +1
#
#i= 0
#while(i < len(l)): #Make sure the iterator is actually increase or infinite loops will occur
#    print l[i]

L = [ i*2 for i in l] # Constructs a list with the first operation over the bounds of a for loop
print L