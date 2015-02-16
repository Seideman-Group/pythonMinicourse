# HOMEWORK make 2 functions one to make a loretnzian approx for arb, bounds, and step size and parameters, and a function taht can check it
from math import pi

def lorentz(x, A, x0, gam):
    return 1/pi * A * 0.5*gam/((x-x0)**2 + (gam*0.5)**2) # Go over this?

def genLoretz(A,x0,gam,lb,ub,step):
    lor = []
    invstep = int(1.0/step) # make the float an int
    for x in range(lb*invstep, ub*invstep, 1):
        lor.append(lorentz(x*step,A,x0,gam))
    return lor

def checkLorntz(lor, A, step):
    s = 0.0
    for l in lor:
        s = s + l * step
    print s
    if( abs(A-s) < A * 0.01):
        print "Lorentz function Approximation is great!"
    elif(abs(A-s) >  A * 0.1):
        print "Lorentz function approximation is bad, please try again"
    else:
        print "Lorentz function approximation is okay, may need to be more accurate"
    
checkLorntz(genLoretz(1.0,1.0,1.0,-90,89, 0.1), 1.0,0.1)