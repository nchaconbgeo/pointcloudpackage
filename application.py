from GUI.Classification.classification import Classification
import tkinter as tk
from GUI import file_select, home_screen
import import_export
import numpy as np
import open3d as o3d
from Visualization import visualization


class Application:
    """
    :Description: Central class that manages core functionality and holds data
    """ 
    root = None
    pointData = None
    fileSelect = None
    open3dVis = None
    geometriesList = []
    homeScreen = None

    def __init__(self):        
        """
        :Description: Create root context and start file select menu
        :return: Application
        """ 
        # creates a Tk() object
        self.root = tk.Tk()
        self.root.withdraw()
        self.fileSelect = file_select.FileSelect(self.root, self.doneSelectingFile, closeFunction = self.closeApp)
        # mainloop, runs infinitely
        tk.mainloop()   

    def closeApp(self):
        """
        :Description: destroy the root context and any active visualizers
        """
        #TODO: Open3d -- Clear geometries and kill visualizer (clean-up)
        self.root.destroy()

    def doneSelectingFile(self):
        """
        :Description: callback function to proceed from selection menu to home screen
        """

        fileFormat = self.fileSelect.formatEntry.get().lower()
        fileName = self.fileSelect.selectedFile
        self.pointData = import_export.readData(fileName, fileFormat)

        if self.pointData == None: #if format is invalid, return to file selection menu
            return

        self.fileSelect.frame.destroy()

        self.open3dVis = o3d.visualization.Visualizer()
        self.geometriesList.append(self.pointData.pointCloud)

        self.homeScreen = home_screen.HomeScreen(self.root, self, closeFunction = self.closeApp)




    def startViewer(self):
        """
        :Description: callback function to create a visualizer to view the cloud without editing
        """
        self.homeScreen.frame.withdraw()  #hide home screen while visualizer is up
        self.open3dVis = o3d.visualization.Visualizer() #create visualizer object
        visualization.visualize(self.open3dVis, self.geometriesList) #Visualize object for user. 
        self.homeScreen.frame.deiconify() #reshow home screen after visualizer closes

    def startVolumeSelector(self):
        """
        :Description: callback function to create a visualizer with editing 
        """
        self.homeScreen.frame.withdraw()  #hide home screen while visualizer is up

        self.open3dVis = o3d.visualization.VisualizerWithEditing()

        visualization.visualize(self.open3dVis, self.geometriesList) #Visualize object for user.
        self.pointData.processLabels(self.open3dVis, self.pointData.selectedIndex)

        self.homeScreen.frame.deiconify() #reshow home screen after visualizer closes

if(__name__ == "__main__"):
    app = Application()