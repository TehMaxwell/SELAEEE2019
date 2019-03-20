"""
AUTHOR: Sam Maxwell
DATE: 25/02/2019

This software allows users to modulate a simple Amplitude Modulated signal in order to "establish" 
communication with a Lunar Base. The aim is to teach students about communication electronics 
and the sort of signals that are used to communicate in space.
"""
#-----------------------------------------------------------------------------------------------------
#MODULES
#-----------------------------------------------------------------------------------------------------
from PyQt5 import QtGui, QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys
import numpy as np

#-----------------------------------------------------------------------------------------------------
#CLASSES
#-----------------------------------------------------------------------------------------------------
#APPLICATION CLASSES
#Class used to generate the QT Application
class appSineWaves(QtWidgets.QApplication):
    #Constructor, generates a new Sine Waves Application
    def __init__(self):
        #Inheriting from the QApplication Class
        super(appSineWaves, self).__init__(sys.argv)

        #Generating the Application Main Window
        mainWindowInstance = mainWindowEventHandler()

        #Executing the Application and Exiting Application when the Window Closes
        sys.exit(self.exec_())

#WINDOW CLASSES
#Class used to generate the Main Window
class mainWindow(QtWidgets.QWidget):
    #DEFINITIONS
    #Window Attributes
    windowWidth = 1600
    windowHeight = 900
    windowTitle = "SELA EEE Activity - Sine Wave Modulation"

    #Constructor, generates a new Main Window
    def __init__(self):
        #Inheriting from the QWidget Class
        super(mainWindow, self).__init__()

        #Setting the window parameters
        self.setWindowTitle(self.windowTitle)
        self.resize(self.windowWidth, self.windowHeight)

        #Building the Window Layout and adding Widgets
        self.gridLayout = QtWidgets.QGridLayout()

        self.graphingCanvas = matplotlibGraph()
        self.gridLayout.addWidget(self.graphingCanvas, 1, 0, 4, 6)

        self.graphingToolbar = matplotlibToolbar(self, self.graphingCanvas)
        self.gridLayout.addWidget(self.graphingToolbar, 0, 0, 1, 6)

        self.carrierFrequencySlider = slider(1000, 100000)
        self.gridLayout.addWidget(self.carrierFrequencySlider, 6, 0, 1, 3)

        self.modulationFrequencySlider = slider(0, 2000)
        self.gridLayout.addWidget(self.modulationFrequencySlider, 6, 3, 1, 3)

        self.amplitudeSlider = slider(0, 10)
        self.gridLayout.addWidget(self.amplitudeSlider, 8, 0, 1, 3)

        self.carrierFrequencyNumber = label("0.0")
        self.gridLayout.addWidget(self.carrierFrequencyNumber, 5, 1, 1, 2)

        self.modulationFrequencyNumber = label("0.0")
        self.gridLayout.addWidget(self.modulationFrequencyNumber, 5, 4, 1, 2)
        
        self.amplitudeNumber = label("0.0")
        self.gridLayout.addWidget(self.amplitudeNumber, 7, 1, 1, 2)

        self.carrierFrequencyLabel = label("Carrier Frequency:")
        self.gridLayout.addWidget(self.carrierFrequencyLabel, 5, 0, 1, 1)

        self.modulationFrequencyLabel = label("Modulation Frequency:")
        self.gridLayout.addWidget(self.modulationFrequencyLabel, 5, 3, 1, 1)

        self.amplitudeLabel = label("Amplitude:")
        self.gridLayout.addWidget(self.amplitudeLabel, 7, 0, 1, 1)

        #Adding the Grid Layout to the Window Layout
        self.setLayout(self.gridLayout)

        #Showing the Main Window
        self.show()

#EVENT HANDLER CLASSES
#Class used for the Main Window Event Handler
class mainWindowEventHandler():
    #DEFINITIONS
    #AM Double Sideband Function Variables
    seconds = 1
    secondIntervals = 1000
    modulationFrequency = 1000.0
    carrierFrequency = 10000.0
    amplitude = 2

    #Target Signal Variables
    targetModulationFrequency = 0.0 
    targetCarrierFrequency = 0.0
    targetAmplitude = 0.0

    #Constructor, generates a new Main Window
    def __init__(self):
        #Creating an instance of the Main Window
        self.mainWindow = mainWindow()

        #Linking the sliders to their respective actions
        self.mainWindow.modulationFrequencySlider.valueChanged.connect(self.updateUserSignalGraph)
        self.mainWindow.carrierFrequencySlider.valueChanged.connect(self.updateUserSignalGraph)
        self.mainWindow.amplitudeSlider.valueChanged.connect(self.updateUserSignalGraph)

        #Plotting the first randomly generated target graph
        self.updateTargetSignalGraph()
        self.updateUserSignalGraph()

    #Function used to update the Live Graph of the Signal
    def updateUserSignalGraph(self):
        #Pulling the current values from the Sliders
        self.modulationFrequency = self.mainWindow.modulationFrequencySlider.value()
        self.carrierFrequency = self.mainWindow.carrierFrequencySlider.value()
        self.amplitude = self.mainWindow.amplitudeSlider.value()

        #Updating the Carrier and Modulation Frequency Label Values
        self.mainWindow.modulationFrequencyNumber.setText(str(self.modulationFrequency) + "Hz")
        self.mainWindow.carrierFrequencyNumber.setText(str(self.carrierFrequency) + "Hz")
        self.mainWindow.amplitudeNumber.setText(str(self.amplitude) + "V")

        #Generating the new set of values to be displayed based upon the current wave parameters
        timeVals, amplitudeVals = self.generateAMDoubleSideband(self.amplitude, self.modulationFrequency, self.carrierFrequency)

        #Plotting the graph
        self.mainWindow.graphingCanvas.userSignalPlot(timeVals, amplitudeVals)

    #Function used to update the graph of the Target Signal
    def updateTargetSignalGraph(self):
        #Updating the Target Values
        self.targetCarrierFrequency = float(np.random.randint(1000, 1000001))
        self.targetModulationFrequency = float(np.random.randint(0, 2001))
        self.targetAmplitude = float(np.random.randint(0, 11))

        #Generating the new set of values for the AM Double Sideband Signal
        timeVals, amplitudeVals = self.generateAMDoubleSideband(self.targetAmplitude, self.modulationFrequency, self.carrierFrequency)

        #Plotting the new Target Graph
        self.mainWindow.graphingCanvas.userTargetPlot(timeVals, amplitudeVals)

    #Function used to generate an AM Double Side Band Signal
    def generateAMDoubleSideband(self, amplitude, modulationFrequency, carrierFrequency):
        #Generating the new set of values to be displayed based upon the current wave parameters
        timeVals = []
        amplitudeVals = []

        for second in range(0, self.seconds + 1):
            for secondFragment in range(0, self.secondIntervals):
                timeVal = (second + secondFragment / self.secondIntervals) / 1000.0
                amplitudeVal = (amplitude + np.sin(modulationFrequency * np.pi * 2.0 * timeVal)) * np.sin(carrierFrequency * np.pi * 2.0 * timeVal)

                timeVals.append(timeVal)
                amplitudeVals.append(amplitudeVal)

        return timeVals, amplitudeVals

#MATPLOTLIB CLASSES
#Class used to generate the Matplotlib Graph
class matplotlibGraph(FigureCanvas):
    #DEFINITIONS
    #Graph Attributes
    yAxisMin = -10.0
    yAxisMax = 10.0
    gridEnabled = True

    #Data Line Attributes
    userGraphLineColour = "g"
    targetGraphLineColour = "r"

    #Constructor, generates a new matplotlib graph viewer and toolbar
    def __init__(self):
        #Generating the Figure to attach to the Figure Canvas
        self.figure = Figure()
        
        #Inheriting from the Matplotlib Figure Canvas Class
        super(matplotlibGraph, self).__init__(self.figure)
        
        #Generating an Axes to Plot on
        self.ax = self.figure.add_subplot(211)
        self.ax1 = self.figure.add_subplot(212)
    
    #Method used to plot a line graph of the user signal data
    def userSignalPlot(self, dataX, dataY):
        #Clearing Graph and Plotting New Data
        self.ax.clear()
        self.ax.plot(dataX, dataY, self.userGraphLineColour)

        #Setting the Plot Parameters
        self.ax.set_ylim(self.yAxisMin, self.yAxisMax)
        self.ax.grid(self.gridEnabled)

        #Showing new graph
        self.draw()

    #Method used to plot a line graph of the target signal data
    def userTargetPlot(self, dataX, dataY):
        #Clearing Graph and Plotting New Data
        self.ax1.clear()
        self.ax1.plot(dataX, dataY, self.targetGraphLineColour)

        #Setting the Plot Parameters
        self.ax1.set_ylim(self.yAxisMin, self.yAxisMax)
        self.ax1.grid(self.gridEnabled)

        #Showing the new Graph
        self.draw()

#Class used to generate the Matplotlib Toolbar
class matplotlibToolbar(NavigationToolbar):
    #Constructor
    def __init__(self, widget, matplotlibFigureCanvas):
        #Inheriting from the Matplotlib Toolbar Class
        super(matplotlibToolbar, self).__init__(matplotlibFigureCanvas, widget)

#WIDGETS
#A widget for the GUI sliders
class slider(QtWidgets.QSlider):
    #Definitions
    minimumVal = 0
    maximumVal = 1000000

    #Constructor
    def __init__(self, minimumSliderVal, maximumSliderVal):
        #Inherting from the QtWidgets Slider Class
        super(slider, self).__init__(QtCore.Qt.Horizontal)

        #Setting Slider Range Variables
        self.minimumVal = minimumSliderVal
        self.maximumVal = maximumSliderVal

        #Setting the attributes of the Slider
        self.setMinimum(self.minimumVal)
        self.setMaximum(self.maximumVal)
        self.TickPosition(self.NoTicks)

#A widget for GUI text displays
class label(QtWidgets.QLabel):
    #Definitions

    #Constructor
    def __init__(self, labelText):
        #Inheriting from the QtWidgets Label Class
        super(label, self).__init__(labelText)

        #Setting the attributes of the label
        self.newFont = font()
        self.setFont(self.newFont)

#A widget for text fonts
class font(QtGui.QFont):
    #Definitions
    fontSize = 20

    #Constructor
    def __init__(self):
        #Inheriting from the QtGui Font Class
        super(font, self).__init__()
        
        #Setting the attributes of the font
        self.setBold(True)
        self.setPointSize(self.fontSize)
        self.setFamily("Calibri")
#-----------------------------------------------------------------------------------------------------
#MAIN CODE
#-----------------------------------------------------------------------------------------------------
application = appSineWaves()