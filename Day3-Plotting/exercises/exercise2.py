#!/usr/bin/env python2.7

'''
The goal of this exercise is to plot data scraped from all the files in a
directory.
'''

from glob import glob
import numpy as np
import matplotlib.pyplot as plt

# hint: "../../day2data/R6G_CWUHVTERS/*.txt"

### get all the file names
# hint: this should be very familiar
filez = glob("day2Data/qChemOutput/*.out")

### get the converged energy from each file, then store the angle and energy in
### numpy arrays
# hint: np.zeros((x)) creates an empty numpy array of length x. ((You need both
# sets of parens))
# hint: enumerate()
angles = np.zeros((len(filez)))
energies = np.zeros((len(filez)))

for ii, qc in enumerate(filez):
    # get the angle
    bits = qc.split("-")
    angle = bits[-1].split(".")[0] # split last element of `bits`, then take first element in that list
    angles[ii] = float(angle)

    # get the energy
    f = open(qc, "r")
    for line in f.readlines():
        if ("Convergence" in line):
            energies[ii] = line.split()[1]
    f.close()

### make a plot of energy vs. angle with red points, and label the axes
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(angles, energies, "ro")
ax.set_title("Potential surface")
ax.set_xlabel("Angle")
ax.set_ylabel("Energy (a.u.)")

fig.savefig("doors.png")