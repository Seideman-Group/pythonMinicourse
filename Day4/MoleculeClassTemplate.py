"""
Objective: Make class for atoms and molecules which extracts information from a QChem output file
Steps:
    Examine the .out files to understand the format and identify where the information you need is located
    Write some pseudo code
    Possible outlines for these classes are provided below
"""

from atomDict import elementMasses #We've provided a resource to get all the masses of elements you need
import os
import numpy as np
import matplotlib.pyplot as plt

class Atom:
    """
    Atoms: storage class (i.e. no functions other than __init__)
    TODO: store these data in the class
        coordinates
        element name
        mass of atom (use atomDict.py to get this info)
    """

    def __init__(self, name, X, Y, Z):
        ########### Fill in ################


class Molecule:
    """
    Molecule: constructs a group of atoms from a .out file
        TODO: store these data:
            number of atoms
            List of Atoms (coordinates and names) - use the Atom class you already made
            Energy
            Source file name
            name of molecule
        functions:
            __init__(self, filename, molname):
                fills data
                    get list of atoms, place in array
                    extract coordinate information
                    grab energy for the converged calculation

            centerOfMass(self):
                calculates the center of mass

            distance(self,n,m):
                calculate the distance between the nth and mth atom

            printCoords(self):
                nicely print the coordinates of all the atoms in the molecule

            plotEnergyConvergence(self):
                plot the energy vs computational cycle
                remember, exclude the last energy from the single point calculation
    """
    #Hint: Here are some terms you can search for (ctrl-F or cmd-F) in the output files as you try to make heads or tails of these things.
    #["Optimization Cycle:","OPTIMIZATION CONVERGED ", "Energy is", "Geometry Optimization Parameters", "User input"]
    #These may not be the key terms you end up using in your code, but they are intended to help you understand the structure of the file.
    def __init__(self, filename, moleculeName):
        if not os.path.isfile(filename):
            raise Exception("Molecule object needs a valid filename")
        ########### Fill in ################

        # Open the file, grab the energies

        # Get the number of atoms

        # Find where in the file the coordinates are stored

        # populate the atom list

    def printCoords(self):
       ########### Fill in ################

    def distance(self,n,m):
       ########### Fill in ################

    def centerofMass(self):
       ########### Fill in ################
       # Forget what a center of mass is?
       # Try: http://en.wikipedia.org/wiki/Center_of_mass

    def plotEnergyConvergence(self):
        ########### Fill in ################



# Test the class
# Note: these are our tests of how we wrote the class; your implementation may
# be different and so may your tests.

Mol = Molecule("CO.out","CO")

for a in Mol.atoms:
    print a.z

Mol.printCoords()

print Mol.distance(0,1)

print Mol.centerofMass()

Mol.plotEnergyConvergence()

# do the same for CHI3
