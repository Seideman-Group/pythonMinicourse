class atom:
    def __init__(self,element, x, y, z):
        self.x_       = x
        self.y_       = y
        self.z_       = z
        self.element_ = element
        self.mass_    = self.getMass()
    def setX(self, x):
        self.x_ = x

    def setY(self, y):
        self.y_ = y

    def setZ(self, z):
        self.z_ = z

    def getMass(self):
        if(self.element_ == 'H'):
            return 1.00794
        elif(self.element_ == 'He'):
            return 4.002602
        elif(self.element_ == 'Li'):
            return 6.941
        elif(self.element_ == 'Be'):
            return 9.012182
        elif(self.element_ == 'B'):
            return 10.811
        elif(self.element_ == 'C'):
            return 12.0107
        elif(self.element_ == 'N'):
            return 14.0067
        elif(self.element_ == 'O'):
            return 15.9994
        elif(self.element_ == 'F'):
            return 18.9984032
        elif(self.element_ == 'Ne'):
            return 20.1797
        elif(self.element_ == 'Na'):
            return 22.98977
        elif(self.element_ == 'Mg'):
            return 24.305
        elif(self.element_ == 'Al'):
            return 26.981538
        elif(self.element_ == 'Si'):
            return 28.0855
        elif(self.element_ == 'P'):
            return 30.973761
        elif(self.element_ == 'S'):
            return 32.065
        elif(self.element_ == 'Cl'):
            return 35.453
        elif(self.element_ == 'Ar'):
            return 39.948
        elif(self.element_ == 'K'):
            return 39.0983
        elif(self.element_ == 'Ca'):
            return 40.078
        elif(self.element_ == 'Sc'):
            return 44.95591
        elif(self.element_ == 'Ti'):
            return 47.867
        elif(self.element_ == 'V'):
            return 50.9415
        elif(self.element_ == 'Cr'):
            return 51.9961
        elif(self.element_ == 'Mn'):
            return 54.938049
        elif(self.element_ == 'Fe'):
            return 55.845
        elif(self.element_ == 'Co'):
            return 58.9332
        elif(self.element_ == 'Ni'):
            return 58.6934
        elif(self.element_ == 'Cu'):
            return 63.546
        elif(self.element_ == 'Zn'):
            return 65.409
        elif(self.element_ == 'Ga'):
            return 69.723
        elif(self.element_ == 'Ge'):
            return 72.64
        elif(self.element_ == 'As'):
            return 74.9216
        elif(self.element_ == 'Se'):
            return 78.96
        elif(self.element_ == 'Br'):
            return 79.904
        elif(self.element_ == 'Kr'):
            return 83.798
        elif(self.element_ == 'Rb'):
            return 85.4678
        elif(self.element_ == 'Sr'):
            return 87.62
        elif(self.element_ == 'Y'):
            return 88.90585
        elif(self.element_ == 'Zr'):
            return 91.224
        elif(self.element_ == 'Nb'):
            return 92.90638
        elif(self.element_ == 'Mo'):
            return 95.94
        elif(self.element_ == 'Tc'):
            return 97.907216
        elif(self.element_ == 'Ru'):
            return 101.07
        elif(self.element_ == 'Rh'):
            return 102.9055
        elif(self.element_ == 'Pd'):
            return 106.42
        elif(self.element_ == 'Ag'):
            return 107.8682
        elif(self.element_ == 'Cd'):
            return 112.411
        elif(self.element_ == 'In'):
            return 114.818
        elif(self.element_ == 'Sn'):
            return 118.71
        elif(self.element_ == 'Sb'):
            return 121.76
        elif(self.element_ == 'Te'):
            return 127.6
        elif(self.element_ == 'I'):
            return 126.90447
        elif(self.element_ == 'Xe'):
            return 131.293
        elif(self.element_ == 'Cs'):
            return 132.90545
        elif(self.element_ == 'Ba'):
            return 137.327
        elif(self.element_ == 'La'):
            return 138.9055
        elif(self.element_ == 'Ce'):
            return 140.116
        elif(self.element_ == 'Pr'):
            return 140.90765
        elif(self.element_ == 'Nd'):
            return 144.24
        elif(self.element_ == 'Pm'):
            return 144.912744
        elif(self.element_ == 'Sm'):
            return 150.36
        elif(self.element_ == 'Eu'):
            return 151.964
        elif(self.element_ == 'Gd'):
            return 157.25
        elif(self.element_ == 'Tb'):
            return 158.92534
        elif(self.element_ == 'Dy'):
            return 162.5
        elif(self.element_ == 'Ho'):
            return 164.93032
        elif(self.element_ == 'Er'):
            return 167.259
        elif(self.element_ == 'Tm'):
            return 168.93421
        elif(self.element_ == 'Yb'):
            return 173.04
        elif(self.element_ == 'Lu'):
            return 174.967
        elif(self.element_ == 'Hf'):
            return 178.49
        elif(self.element_ == 'Ta'):
            return 180.9479
        elif(self.element_ == 'W'):
            return 183.84
        elif(self.element_ == 'Re'):
            return 186.207
        elif(self.element_ == 'Os'):
            return 190.23
        elif(self.element_ == 'Ir'):
            return 192.217
        elif(self.element_ == 'Pt'):
            return 195.078
        elif(self.element_ == 'Au'):
            return 196.96655
        elif(self.element_ == 'Hg'):
            return 200.59
        elif(self.element_ == 'Tl'):
            return 204.3833
        elif(self.element_ == 'Pb'):
            return 207.2
        elif(self.element_ == 'Bi'):
            return 208.98038
        elif(self.element_ == 'Po'):
            return 208.982416
        elif(self.element_ == 'At'):
            return 209.9871
        elif(self.element_ == 'Rn'):
            return 222.0176
        elif(self.element_ == 'Fr'):
            return 223.0197307
        elif(self.element_ == 'Ra'):
            return 226.025403
        elif(self.element_ == 'Ac'):
            return 227.027747
        elif(self.element_ == 'Th'):
            return 232.0381
        elif(self.element_ == 'Pa'):
            return 231.03588
        elif(self.element_ == 'U'):
            return 238.02891
        elif(self.element_ == 'Np'):
            return 237.048167
        elif(self.element_ == 'Pu'):
            return 244.064198
        elif(self.element_ == 'Am'):
            return 243.061373
        elif(self.element_ == 'Cm'):
            return 247.070347
        elif(self.element_ == 'Bk'):
            return 247.070299
        elif(self.element_ == 'Cf'):
            return 251.07958
        elif(self.element_ == 'Es'):
            return 252.08297
        elif(self.element_ == 'Fm'):
            return 257.095099
        elif(self.element_ == 'Md'):
            return 258.098425
        elif(self.element_ == 'No'):
            return 259.10102
        elif(self.element_ == 'Lr'):
            return 262.10969
        elif(self.element_ == 'Rf'):
            return 261.10875
        elif(self.element_ == 'Db'):
            return 262.11415
        elif(self.element_ == 'Sg'):
            return 266.12193
        elif(self.element_ == 'Bh'):
            return 264.12473
        elif(self.element_ == 'Hs'):
            return 269.13411
        elif(self.element_ == 'Mt'):
            return 268.13882
        else:
            return -9999999.0
