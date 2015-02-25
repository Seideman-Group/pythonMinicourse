from tomAtom import atom
import os
class molecule:
    def __init__(self, fname):
        if not os.path.isfile(fname):
            raise Exception("Molecule object needs a valid filename")
        self.atoms_  = []
        self.energy_ = []
        outFile      = open(fname, 'r')
        lines        = outFile.readlines()
        self.n_opt   = max([int(line.split()[2]) for line in lines if("Optimization Cycle:" in line)])
        energy       = [float(line.split()[3]) for line in lines if("Final energy is " in line)]
        self.energy_ = energy[0]
        ll = 0
        #while( not ("$molecule" in lines[ll])):
        #    ll = ll+1
        #ll = ll+2
        #while( not("$end" in lines[ll])):
        #    # print lines[ll]
        #    atmLine = lines[ll].split()
        #    # print atmLine
        #    # print ll
        #    if(len(atmLine) > 1):
        #        self.atoms_.append(atom(atmLine[0], float(atmLine[1]), float(atmLine[2]), float(atmLine[3])))
        #    ll = ll +1

        for ll in range(len(lines)):
            if("Coordinates (Angstroms)" in lines[ll]):
                if (len(self.atoms_) == 0):
                    print "Getting molecular coords"
                    aa = 2
                    while(not "Point Group:" in lines[ll+aa]):
                        atmLine = lines[ll+aa].split()
                        self.atoms_.append(atom(atmLine[1], float(atmLine[2]), float(atmLine[3]), float(atmLine[4])))
                        aa = aa+1
                else:                 
                    for ii in range(len(self.atoms_)):
                        atmLine = lines[ll+ii+2].split()
                        # print atmLine
                        self.atoms_[ii].x_ = float(atmLine[2])
                        self.atoms_[ii].y_ = float(atmLine[3])
                        self.atoms_[ii].z_ = float(atmLine[4])
    def centerOfMass(self):
        cenMass = [0.0,0.0,0.0]
        mass    = 0.0
        for atm in self.atoms_:
            cenMass[0] = cenMass[0] + atm.x_ * atm.mass_
            cenMass[1] = cenMass[1] + atm.y_ * atm.mass_
            cenMass[2] = cenMass[2] + atm.z_ * atm.mass_
            mass = mass + atm.mass_
        for ii in range(len(cenMass)):
            cenMass[ii] = cenMass[ii] / mass
        return cenMass


mol = molecule("CO.out")
print mol.n_opt
for atm in mol.atoms_:
    print atm.element_
    print atm.mass_
    print atm.x_
    print atm.y_
    print atm.z_
    print "done"
print mol.centerOfMass()
