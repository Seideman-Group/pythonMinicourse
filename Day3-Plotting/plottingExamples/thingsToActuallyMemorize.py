#!/usr/bin/env python2.7

'''
This script demonstrates the bare-bones basics you should memorize about using
matplotlib. The rest you will very likely want to Google for and learn by
studying examples.
'''

# standard nomenclature is `plt`
import matplotlib.pyplot as plt

# you can't have one without the other
import numpy as np

### Prepare the data to plot ###

# This is the variable part. In general you either have data from somewhere to
# plot, or make it up.
x = np.linspace(0, 10, 101)
y = np.sin(np.cos(np.tan(x)))

### Create the plot objects (Figure, Axes) and plot the data

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) # can also do (111) as argument

ax.plot(x, y)

# These examples are useful; uncomment them to see what they do...
# http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.plot for options

# ax.plot(x, y, label="data")
# ax.plot(x, y, 'rx')
# ax.plot(x, y, 'g--')

### Decorate the plot
# http://matplotlib.org/api/axes_api.html
# has a lot of the `set_*` commands

ax.set_xlabel("abscissa")
ax.set_ylabel("ordinate")

### (optional) save image files

fig.savefig("data.pdf") # file type detected automatically, but you can specify

### Draw the plot on screen

plt.show()
