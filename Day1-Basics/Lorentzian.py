import math
#previous work
# Lorentz function is defined defined as 1/pi * A * 1/2Gam/((x-x0)^2 +(1/2Gam)**2)
# write a for loop that can get the values of a lorentzian centered at 5.0 and a width of 2.0 and A = pi from 0 to 10 with a numerical step of 0.01
#for i in range(10*100+1):
#    print str(i*0.01) + " \t " + str(1.0/((i*0.01-5.0)**2 + (1.0)**2 ))

# Using the definition of the Lortenzian you did in the last exercise to calculate the area under a Lorentzian while its value is >= 1e-3
#x = 5.0
#s = 0.0
#while(1.0/((x-5.0)**2 + (1.0)**2) >= 1e-8):
#    s = s + 1.0/((x-5.0)**2 + (1.0)**2) * 0.001
#    x = x + 0.001
#print s * 2 - 0.001

def lorenz(x, center, width, peakhieght):
    return 1.0/math.pi * (0.5*width) / ((x-center)**2 + (0.5*width)**2) * peakhieght*(width*math.pi/2)

def makeLorenz(center, width, peakhieght, tol, step):
    x = center
    lor = []
    xvals=[]
    while(lorenz(x,center, width, peakhieght) >= tol):
        lor.append(lorenz(x,center, width, peakhieght))
        x = x + step
    lor_copy = []
    lor_copy[:] = lor[:]
    lor.reverse()
    lor[len(lor)-1:] = lor_copy[:]
    x = [i*step - step*(len(lor)-1)/2.0 + center for i in range(len(lor)) ]
    return x, lor

def integrate(lor, step):
    s = 0
    for num in lor:
        s = s + num*step
    return s

import matplotlib.pyplot as plt
x, lor = makeLorenz(1.0,2.0,3.0,1e-5,.001)
print integrate(lor, 0.001)
print lor[len(lor)/2-5:len(lor)/2+5]
plt.plot(x, lor)
plt.axis([-4,6,0,3.1])
plt.show()
