def helloPerson(names):
    greeting = "Hello world" #Base string to be manipulated
    greeted = [] #Start a new list for the
    for name in names: #loop over names
        if(not isinstance(name, basestring)): #check if name is not a string
            print greeting # print greeting
        else:
            print greeting[:6] + name # if not print Hello name
            greeted.append(name) #Store name in greeted
    return greeted #return greeted

names =[1, "Tom", "Lindsey", "Bob", "Alice", 5.0, "Schrodinger", True]
g = helloPerson(names)
#print greeted[0]
print g[0]