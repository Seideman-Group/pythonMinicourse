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
    
  
#FindMax takes a list of list as the input and returns a tuple of the max_x and max_y values where max_y is a maximum of the data set  
def FindMax(data):
    #Initially set the maximum as a really small number
    max=-100000000000 
    for row in data:
        if (row[1]>max):
            max_x=row[0]
            max_y=row[1]
            max=row[1]
    return (max_x, max_y)
    
#FindBounds takes in the min x and the max x and returns indexes that inclusively correspond to those min/max for the variable dataset (which is a list of lists) 

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