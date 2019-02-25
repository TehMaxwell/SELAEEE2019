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
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys

#-----------------------------------------------------------------------------------------------------
#CLASSES
#-----------------------------------------------------------------------------------------------------
#APPLICATION CLASSES
#Class used to generate the QT Application
class appSineWaves(QtGui.QApplication):
    #Constructor, generates a new Sine Waves Application
    def __init__(self):
        #Inheriting from the QApplication Class
        super(appSineWaves, self).__init__(sys.argv)

        #Generating the Application Main Window

        #Executing the Application and Exiting Application when the Window Closes
        sys.exit(self.exec_())

#WINDOW CLASSES
#Class used to generate the Main Window
class mainWindow(QtGui.QWidget):
    #DEFINITIONS
    #Window Attributes
    windowWidth = 1600
    windowHeight = 900
    windowTitle = "SELA EEE Activity - Sine Wave Modulation"

    #Constructor, generates a new Main Window
    def __init__(self):
        #Inheriting from the QWidget Class
        super(mainWindow, self).__init__()

        #

#EVENT HANDLER CLASSES
#Class used for the Main Window Event Handler
class mainWindowEventHandler():
    #DEFINITIONS

    #Constructor, generates a new Main Window
    def __init__(self):
        #Creating an instance of the Main Window
        self.mainWindow = mainWindow()

        #

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
        self.ax = self.figure.add_subplot(111)
    
    #Method used to plot a line graph of data
    def linePlot(self, dataX, dataY):
        self.ax.plot(dataX, dataY)
