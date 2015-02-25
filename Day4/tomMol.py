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
        while( not ("$molecule" in lines[ll])):
            ll = ll+1

        ll = ll+2
        while( not("$end" in lines[ll])):
            # print lines[ll]
            atmLine = lines[ll].split()
            # print atmLine
            # print ll
            if(len(atmLine) > 1):
                self.atoms_.append(atom(atmLine[0], float(atmLine[1]), float(atmLine[2]), float(atmLine[3])))
            ll = ll +1

        for ll in range(len(lines)):
            if("Coordinates (Angstroms)" in lines[ll]):
                for ii in range(len(self.atoms_)):
                    atmLine = lines[ll+ii+2].split()
                    # print atmLine
                    self.atoms_[ii].x_ = atmLine[2]
                    self.atoms_[ii].y_ = atmLine[3]
                    self.atoms_[ii].z_ = atmLine[4]



mol = molecule("CHI3.out")
print mol.n_opt
for atm in mol.atoms_:
    print atm.element_
    print atm.x_
    print atm.y_
    print atm.z_
    print "done"
