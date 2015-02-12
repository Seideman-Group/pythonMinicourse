

#Learning Objective 1:Assigning a List of Lists

data=[[100.0, 0.0], [250.0, 100.0], [380.0, 190.0], [400.0, 453.3], [450.0, 124.0], [500.0, 0.0], [600.0, 40.0], [700.0, 38.0], [800.0, 0.0], [900.0, 0.0], [910.0, 0.0], [920.0, 10.0], [930.0, 20.0], [940.0, 50.0], [944.0, 100.0], [945.0, 110.0], [946.0, 100.0], [947.0, 150.0], [948.0, 120.0], [950.0, 100.0]]

print "The data is \n", data

#Let's get a list of the energies.

energies=[]

#Learning Objective 2: Implement a loop
for row in data:
    energies.append(row[0]) #a lot going on here


first_column = [ row[0] for row in data ]

print "\n \n The energies are \n", energies
print "Which is the same as the first column \n", first_column

#And a list of absorbance

absorbance=[]
for row in data:
    absorbance.append(row[1])


second_column = [ row[1] for row in data ]

print "\n \n The absorbance is \n", absorbance


print "The second column is \n", second_column


print "\n The first element in 'data' is ", data[0]

print "The energy of that first data point is ", data[0][0], " nm"

print "The absorbance is ", data[0][1]





#Identify the min and max

#Learning Objective 3: implementing and using a function
#FindMax(data) takes a data, list of tuples, finds the maximum of the absorbance, and returns the tuple that corresponds to that point.

from HelperFunctions import FindMax

maximum=FindMax(data)
print "maximum=", maximum
print "The maximum absorbance of this spectrum is ", maximum[1] , "at ", maximum[0], " nm"

##Demo how does max(data) not work here??

#Identify the min and max of the IR region, vis region, and UV region

#Let's make this an example exercise for the class.  Provide a commented blank file and organize it...




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

from HelperFunctions import FindEnergyBounds

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


