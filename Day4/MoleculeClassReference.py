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
        self.x       = X
        self.y       = Y
        self.z       = Z
        self.element = name.lower()
        self.mass    = elementMasses[self.element]


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
        self.source = filename
        self.name   = moleculeName
        self.atoms  = []

# Open the file, grab the energies
        outFile     = open(filename, 'r')
        lines       = outFile.readlines()
        energies    = [float(line.split()[1]) for line in lines if("Convergence criterion met" in line)]
        self.energy = energies[-1]
        outFile.close()

# Get the number of atoms
        ll = 0 # ll is the index in the array where the atom coordinates are located
        for ii,line in enumerate(lines):
            if "NAtoms," in line:
                self.nAtoms = int(lines[ii+1].split()[0])

# Find where in the file the coordinates are stored
        for ii in range(len(lines)):
            if("Coordinates (Angstroms)" in lines[ii]):
                ll = ii

# populate the atom list
        for ii in range(self.nAtoms):
            atmLine = lines[ll+ii+2].split()
            name = atmLine[1]
            x = float(atmLine[2])
            y = float(atmLine[3])
            z = float(atmLine[4])
            self.atoms.append( Atom(name,x,y,z) )

    def printCoords(self):
        print "name\tX\t\tY\t\tZ"
        for atm in self.atoms:
            print atm.element,'\t',atm.x,'\t',atm.y,'\t',atm.z
            # print "%s\t%.6f\t%.6f\t%.6f" % (atm.element,atm.x,atm.y,atm.z) # Alternate printing method #1
            # print "{name:^15}{x:>15}{y:>15}{z:>15}".format(name=atm.element,x=atm.x,y=atm.y,z=atm.z) # Alternate printing method #2

    def distance(self,n,m):
        return np.sqrt((self.atoms[n].x-self.atoms[m].x)**2 + (self.atoms[n].y-self.atoms[m].y)**2 + (self.atoms[n].z-self.atoms[m].z)**2)

    def centerofMass(self):
        cenMass = np.zeros(3)
        totalMass = 0.0
        for atm in self.atoms:
            cenMass[0] = cenMass[0] + atm.x * atm.mass
            cenMass[1] = cenMass[1] + atm.y * atm.mass
            cenMass[2] = cenMass[2] + atm.z * atm.mass
            totalMass = totalMass + atm.mass
        for ii in range(len(cenMass)):
            cenMass[ii] = cenMass[ii] / totalMass
        return cenMass

    def plotEnergyConvergence(self):
        inFile = open(self.source)
        lines = inFile.readlines()
        inFile.close()
        energies = np.array([float(line.split()[1]) for line in lines if("Convergence criterion met" in line)])
        plt.plot(energies[:-1],'ro-')
        plt.xlabel("Step")
        plt.ylabel("Energy / au")
        plt.title("Energy Convergence of " + self.name)
        plt.show()


# Test the class

Mol = Molecule("CO.out","CO")
for a in Mol.atoms:
    print a.z
print Mol.centerofMass()
print Mol.distance(0,1)

Mol.printCoords()
Mol.plotEnergyConvergence()

Mol2 = Molecule("CHI3.out",r"CHI$_3$")
for a in Mol2.atoms:
    print a.z
print Mol2.centerofMass()
print Mol2.distance(0,1)

Mol2.printCoords()
Mol2.plotEnergyConvergence()
