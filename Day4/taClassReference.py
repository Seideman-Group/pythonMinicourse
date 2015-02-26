import numpy as np

### define class

class TASpectrum:
    def __init__(self, fileName):
        '''
        Store information from TA data file.

        The data format is:
            - first row: dummy value (0.0) followed by time points in ps
            - first column: dummy value (0.0) followed by wavelengths in nm
            - other rows/columns: transient absorption values
            - metadata:
                - Date
                - Sample
                - Solvent
                - Pump energy:
                - Pump wavelength (nm):
                - Cuvette length (mm):
                - Comments: Averaging time:
                - Number of scans:
                - Time units:
                - Z axis title:
        '''

        ### set default values for metadata
        # hint: to thine own `self` be true

        self.date = "today"
        self.sample = "DEFAULT"
        self.solvent = "DEFAULT"
        self.pumpEnergy = 0.0
        self.pumpWavelength = 0.0
        self.cuvetteLength = 10.0
        self.comments = ""
        self.numberScans = 1
        self.timeUnits = "ps"
        self.zAxisTitle = "z data"

        ### read in matrix of data
        # hint: look up genfromtxt parameters
        self.rawData = np.genfromtxt(fileName, delimiter=",", invalid_raise=False)

        # break apart (index) matrix to get times, wavelengths and actual data
        self.times = self.rawData[0,1:]
        self.wavelengths = self.rawData[1:,0]
        self.data = self.rawData[1:,1:]

        # check for bad data (NaN values)
        # hint: you can just delete the first 13 lines of data, or you can find
        # an automatic way to delete bad rows of data (harder than it sounds).
        # Remember to keep the array of wavelengths with the same number of rows
        # as the array of data.

        self.wavelengths = self.wavelengths[13:]
        self.data = self.data[13:,:]

        ### read in metadata
        # hint: maybe just go line-by-line
        # hint: this string method may be useful: "--".join(["one", "II", "c"])
        inputFile = open(fileName, "r")

        # check each line for all parameters
        for line in inputFile.readlines():
            if "Date" in line:
                self.date = " ".join(line.split()[2:])
            elif "Sample" in line:
                self.sample = " ".join(line.split()[1:])
            elif "Solvent" in line:
                self.solvent = " ".join(line.split()[1:])
            elif "Pump energy" in line:
                self.pumpEnergy = " ".join(line.split()[2:])
            elif "Pump wavelength" in line:
                self.pumpWavelength = " ".join(line.split()[3:])
            elif "Cuvette length" in line:
                self.cuvetteLength = " ".join(line.split()[3:])
            elif "Comments" in line:
                self.comments = " ".join(line.split()[1:])
            elif "Number of scans" in line:
                self.numberScans = " ".join(line.split()[3:])
            elif "Time units" in line:
                self.timeUnits = " ".join(line.split()[2:])
            elif "Z axis title" in line:
                self.zAxisTitle = " ".join(line.split()[3:])

        inputFile.close()