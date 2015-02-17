# HOMEWORK make 2 functions one to make a loretnzian approx for arb, bounds, and step size and parameters, and a function taht can check it
from math import pi


def lorentz(x, A, x0, gam):
    # Take in parameters for the lorentzian and the point of interest
    # x: The point
    # A: The Amplitude
    # x0 : the center point
    # gam: The width 
    # Return the value of the lorentizian at that point
    return 1/pi * A * 0.5*gam/((x-x0)**2 + (gam*0.5)**2) # Go over this?

def genLoretz(A,x0,gam,lb,ub,step):
    # Take in parameters for the lorentzian and the parameters describing the range of where you want to define the function
    # A: The Amplitude
    # x0 : the center point
    # gam: The width 
    # lower bound for x
    # upper bound for x
    # iteration step
    # Return a list of floats describing the lorentzian in the specified range
    lor = []
    invstep = int(1.0/step) # make the float an int
    for x in range(lb*invstep, ub*invstep, 1):
        lor.append(lorentz(x*step,A,x0,gam))
    return lor

def checkLorntz(lor, A, step):
    # Take in a list describing the lorentzian and integration parameters, print out the accuracy of the computation
    # lor A list describint the lorentzian
    # A the Amplitude of the Lorentizian
    # step iteration step used to generate the list
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