"""
Objectives for Day 3 Part 1:
    - Import spectral data into python using classes
    - Make a really simple plot
    - Data manipulations
        - Smoothing
        - Baseline correction
        - Curve fitting
    - Really simple heat map

Note: Change the plotting format to SVG in preferences
Note: Also, Change the directory before using this script
"""

# Import all the modules




# Import the x-axis
# Load all spectra into an array, first get all file names, then create Spectrum objects




# Let's sort them based on the appropriate number




# Let's make a basic plot of one of the data sets



# Let's just work with one piece for now


##########################################
# Noise  Correction and baseline fitting
##########################################

#import the scipy signal library


# Median filter



# plt.plot(xData,yData_med)
# plt.title("Median Line Filter")
# plt.show()

# Savitsky-Golay filter



# plt.plot(xData,yData_sav)
# plt.title("Savitsky-Golay Filter")
# plt.show()

# baseline fitting





#plt.plot(xData,baseline)
#plt.title("Crude Baseline")
#plt.show()


# Now let's correct the baseline to make it a bit smoother





#plt.plot(xData,baseline, xData, yData)
#plt.title("Corrected Baseline")
#plt.show()

# Finally subtract the baseline




#plt.plot(xData, modData, xData, yData-baseline)
#plt.title("Savitsky-Golay Filter, Baseline Subtracted")
#plt.show()

############################################################
# Peak Finding - Check scipy signal library for more options
############################################################

# finds all local max in smoothed data set
# filter out those that are too small









#plt.gcf().set_size_inches(16.0,12.0)
#plt.plot(xData, modData)
#plt.plot(xData[peaks], modData[peaks],'ro')
#plt.show()

###################################################
# Curve Fitting - one of the most requested topics
###################################################









#plt.gcf().set_size_inches(16.0,12.0)
#plt.plot(xData, modData)
#plt.plot(xData, reprodData)
#plt.show()

#plt.gcf().set_size_inches(16.0,12.0)
#plt.plot(xData, yData,)
#plt.plot(xData,reprodData+baseline,linewidth=2.0,color="black")
#plt.title("Fully fitted spectrum")
#plt.show()

# Convert to 2D array of spectra











#plt.axis([min(xData),max(xData),0, len(spectra)])
#plt.xlabel(r'Wavenumber / cm$^{-1}$')
#plt.ylabel("Number")
#plt.show()