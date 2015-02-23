#!/usr/bin/env python2.7

'''
This script demonstrates three ways to make the same plot with matplotlib.

These are the most common coding styles that you may encounter when looking for
examples of plots online.
'''

### Resources
# FAQ: http://matplotlib.org/faq/usage_faq.html
# Figure commands: http://matplotlib.org/api/figure_api.html
# Axes commands: http://matplotlib.org/api/axes_api.html

import matplotlib.pyplot as plt
import numpy as np



### First way: quick and dirty
# Good for simple plots or interactive data exploration.

# create data
x = np.linspace(0, 4*np.pi, 101)
y = np.tan(x)

# plot the data: memorize this basic sequence
plt.plot(x, y)                    # 1: plot data

plt.title("Quick and dirty way")  # 2: decorate plot (optional)
plt.xlabel("x")
plt.ylabel("y")

plt.show()                        # 3: draw plot



### Second way: manipulating axes, figure objects
# Most general technique. Highly recommended for more complex plots.

# memorization optional... copy/paste is your friend
fig = plt.figure()                # The figure object contains one or more Axes.

ax = fig.add_subplot(1,1,1)       # An Axes object is what you see as a plot.

ax.plot(x, y)                     # Axes commands are what you use for plotting
ax.set_title("More general way")  # and decorating the plot. Many Axes commands
ax.set_xlabel("x")                # with `set_*` have a counterpart in the
ax.set_ylabel("y")                # pyplot namespace (e.g. `set_title`, `title`)

plt.show()



### Third way: pylab
# Less standard, so less recommended. Can be convenient though.

del x, y # clear data variables from earlier; they will soon be born again

import pylab as pl # matplotlib + numpy in one namespace

# This is the same as the first example, but it is a bit more MATLAB-y because
# all the numpy and plotting commands are available under pylab (pl).
x = pl.linspace(0, 4*pl.pi, 101)
y = pl.tan(x)

pl.plot(x, y)
pl.title("pylab")
pl.xlabel("x")
pl.ylabel("y")

pl.show()

print("foo")
