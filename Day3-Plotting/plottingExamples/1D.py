#!/usr/bin/env python2.7

import numpy as np
# pyplot documentation: http://matplotlib.org/api/pyplot_api.html
import matplotlib.pyplot as plt

# make up some x and y data
x = np.linspace(0, 10, 101)
y = np.sin(x)
y2 = y + np.random.random(np.size(y)) * 0.2 - 0.1 # y plus noise

# set up plot object
plt.xlabel("Time")
plt.ylabel("Signal")

### Things to include
# decorating plots with labels
# mention you can set things in plot command or with set_* commands, link to dox

# plot lines
plt.plot(x, y, label="Ideal signal", linewidth=2)
# every time you call the `plot` command on the plot object, a new line is added
plt.plot(x, y2, label="Measured signal", linewidth=2)

# add a legend
plt.legend()

# the plot is only drawn when the `show` command is issued
plt.show()