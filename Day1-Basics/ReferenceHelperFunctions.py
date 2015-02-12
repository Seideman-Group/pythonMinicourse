

#LoadData takes a string with the file name as input and gives a list of lists containing the data as output

def LoadData(filename):
    print filename
    data=[]
    file=open(filename, 'r')
    for line in file:
        x=float(line.split()[0])
        y=float(line.split()[1])
        #print x,y
        data.append([x,y])
        
    return data
    
#Learning Objective 3: Implement and Use a function

#FindMax takes a list of lists as the input and returns two values,  max_x and max_y, such that max_y is a maximum of the data set  
#def indicates this is a function
#FindMax is the function's name
#dataList is the input variable. For this function to work as written it must be a list of lists 
def FindMax(dataList):
    #Initially set the maximum as a really small number
    max_y=-100000000000 ###point of discussion 
    #max_y=None  #Or this
    #max_y=data[0][1]  #Or this
    #For each data point in the dataList, if the second value is greater than the current max value, save that max_y and the corresponding max_x
    for row in dataList:
        if (row[1]>max_y):
            max_x=row[0]
            max_y=row[1]
    #return max_y        #Why just return one value?
    return max_x, max_y  #When we can return more than one value.
    


## FindEnergyBounds takes in the min and the max for some region of wavelengths and returns indexes of a list of lists 
## that inclusively correspond to those min/max for the variable dataset (which is a list of lists) 

def FindEnergyBounds(min,max,data):
    i=0
    min_i=0
    max_i=0
    for row in data:
        i=i+1
        if row[0]<=max:
            max_i=i
        if not row[0]>min:
            min_i=i
    print min_i, max_i
    return min_i, max_i