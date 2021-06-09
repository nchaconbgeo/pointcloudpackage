import tkinter as tk
from GUI import file_select, home_screen
import import_export
import numpy as np
import open3d as o3d
from Visualization import visualization


class Application:
    root = None
    pointData = None
    fileSelect = None
    open3dVis = None
    geometriesList = []
    homeScreen = None

    def __init__(self):
        # creates a Tk() object
        self.root = tk.Tk()
        self.root.withdraw()
        self.fileSelect = file_select.FileSelect(self.root, self.doneSelectingFile, closeFunction = self.closeApp)
        # mainloop, runs infinitely
        tk.mainloop()   

    def closeApp(self):
        #TODO: Open3d -- Clear geometries and kill visualizer (clean-up)
        self.root.destroy()

    def doneSelectingFile(self):
        fileFormat = self.fileSelect.formatEntry.get().lower()
        fileName = self.fileSelect.selectedFile
        self.pointData = import_export.readData(fileName, fileFormat)

        if self.pointData == None: #if format is invalid, return to file selection menu
            return

        self.fileSelect.frame.destroy()
        self.open3dVis = o3d.visualization.Visualizer()
        self.geometriesList.append(self.pointData.pointCloud)

        #Visualize object for user. 
        visualization.visualize(self.open3dVis, self.geometriesList)
        self.homeScreen = home_screen.HomeScreen(self.root, self, closeFunction = self.closeApp)

if(__name__ == "__main__"):
    app = Application()