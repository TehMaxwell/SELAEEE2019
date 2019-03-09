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

        self.carrierFrequencySlider = slider()
        self.gridLayout.addWidget(self.carrierFrequencySlider, 7, 0, 1, 3)

        self.modulationFrequencySlider = slider()
        self.gridLayout.addWidget(self.modulationFrequencySlider, 7, 3, 1, 3)

        self.carrierFrequencyNumber = label("0.0")
        self.gridLayout.addWidget(self.carrierFrequencyNumber, 6, 0, 1, 3)

        self.modulationFrequencyNumber = label("0.0")
        self.gridLayout.addWidget(self.modulationFrequencyNumber, 6, 3, 1, 3)

        self.carrierFrequencyLabel = label("Carrier Frequency:")
        self.gridLayout.addWidget(self.carrierFrequencyLabel, 5, 0, 1, 3)

        self.modulationFrequencyLabel = label("Modulation Frequency:")
        self.gridLayout.addWidget(self.modulationFrequencyLabel, 5, 3, 1, 3)

        #Adding the Grid Layout to the Window Layout
        self.setLayout(self.gridLayout)

        #Showing the Main Window
        self.show()

#EVENT HANDLER CLASSES
#Class used for the Main Window Event Handler
class mainWindowEventHandler():
    #DEFINITIONS

    #Constructor, generates a new Main Window
    def __init__(self):
        #Creating an instance of the Main Window
        self.mainWindow = mainWindow()

#MATPLOTLIB CLASSES
#Class used to generate the Matplotlib Graph
class matplotlibGraph(FigureCanvas):
    #DEFINITIONS

    #Constructor, generates a new matplotlib graph viewer and toolbar
    def __init__(self):
        #Generating the Figure to attach to the Figure Canvas
        self.figure = Figure()
        
        #Inheriting from the Matplotlib Figure Canvas Class
        super(matplotlibGraph, self).__init__(self.figure)
        
        #Generating an Axes to Plot on
        self.ax = self.figure.add_subplot(211)
        self.ax1 = self.figure.add_subplot(212)
    
    #Method used to plot a line graph of data
    def linePlot(self, dataX, dataY):
        self.ax.plot(dataX, dataY)

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
    maximumVal = 1000

    #Constructor
    def __init__(self):
        #Inherting from the QtWidgets Slider Class
        super(slider, self).__init__(QtCore.Qt.Horizontal)

        #Setting the attributes of the Slider
        self.setMinimum = self.minimumVal
        self.setMaximum = self.maximumVal
        self.TickPosition = self.NoTicks

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