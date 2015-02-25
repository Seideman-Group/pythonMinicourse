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
        coordinates
        element name
        mass of atom (use atomDict.py to get this info)
    """
    def __init__(self, name, X, Y, Z):
        ########### Fill in ################


class Molecule:
    """
    Molecule: constructs a group of atoms from a .out file
        data:
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
    def __init__(self, filename, moleculeName):
        if not os.path.isfile(filename):
            raise Exception("Molecule object needs a valid filename")
       ########### Fill in ################

    def centerofMass(self):
       ########### Fill in ################
       # Forget what a center of mass is?
       # Try: http://en.wikipedia.org/wiki/Center_of_mass


    def printCoords(self):
       ########### Fill in ################

    def distance(self,n,m):
       ########### Fill in ################

    def plotEnergyConvergence(self):
        ########### Fill in ################



# Test the class
