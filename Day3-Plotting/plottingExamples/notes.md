# plotting notes

# Recommended reading before class
- Usage FAQ: a good reference to clear up common confusions when learning matplotlib
  - http://matplotlib.org/faq/usage_faq.html (read from start through "Coding Styles")

# Sometimes there is more than one way to do the same thing.
- Examples of plotting sin(x) (`moreThanOneWayToDoIt.py`)
  - basic matplotlib
  - manipulating figure, axis objects
  - pyplot
- What are the modules involved?
  - matplotlib: plotting library designed to work with numpy/scipy
  - pyplot: a MATLABesque container module that rolls matplotlib/numpy/scipy into one

# Choose your level of complexity
- Just looking at data: `plot` and `show`
- Well-groomed simple plots
  - prepare data
  - plot data
  - adjust plot parameters (Googling is usually necessary)
    - axis labels
    - ticks
    - legend
    - color maps
  - show
- Subfigures, arrows

# Specific Examples
- Josh: 1D plots
- Josh: van Duyne group spectra
- Andy: 2D plots
- Andy: subplots
- Andy: loaf

# Resources
- Gallery (fancy examples): http://matplotlib.org/gallery.html
- more basic examples: http://matplotlib.org/users/screenshots.html
- http://matplotlib.org/api/pyplot_api.html




### thingsToActuallyMemorize.py
- once you have data, you need two commands: plot() and show()
- 5 steps: prepare, plot(), decorate, output to screen and/or file

- QUESTION: what to do to plot data from 2col.dat?

### moreThanOneWayToDoIt.py
- I showed you the basic way.
- fig, ax objects for more advanced plots
- ASIDE: matplotlib FAQ
- also pylab is a thing

### 2D.py
- ASIDE: 2D lorentzian
- ASIDE: meshgrid

###
