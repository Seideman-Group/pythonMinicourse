import math

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
