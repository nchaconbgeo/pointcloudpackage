from point_data import PointData
from GUI.Classification.classification import Classification
import tkinter as tk
from GUI import file_select, home_screen
import import_export
import numpy as np
import open3d as o3d
from Visualization import visualization
from tkinter import colorchooser
import os


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
    fileFormat = None
    fileName = None
    LINE_COLOR_PROMPT =  "Choose Line Color"
    chosenLineColor = None

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

        self.fileFormat = self.fileSelect.formatEntry.get().lower()
        self.fileName = self.fileSelect.selectedFile
        self.pointData = import_export.readData(self.fileName, self.fileFormat)

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


    def drawLine(self):
        self.homeScreen.frame.withdraw()  #hide home screen while visualizer is up
        self.open3dVis = o3d.visualization.VisualizerWithEditing()
        linePoints, indices = visualization.drawLines(self.open3dVis, self.geometriesList, self.pointData.pointCloud) #Visualize object for user.

        color = colorchooser.askcolor(title = self.LINE_COLOR_PROMPT)[1] #color code is the 2nd argument returned by the color chooser
        if color != None: #cancelling yields a result of None
            self.chosenLineColor = color
        else:
            self.chosenLineColor = '#ffffff'
           
        #convert color from hex to rgb for lineset.
        rgbColor = np.asarray(tuple(float(int(self.chosenLineColor[i:i+2], 16)) / 255 for i in (1, 3, 5)))
        colorsList = [rgbColor for i in range(len(indices))]

        lineSet = o3d.geometry.LineSet()
        lineSet.colors = o3d.utility.Vector3dVector(colorsList)
        lineSet.points = o3d.utility.Vector3dVector(linePoints)
        lineSet.lines = o3d.utility.Vector2iVector(indices)
        self.geometriesList.append(lineSet)
        self.homeScreen.frame.deiconify()



    def exportRecolored(self):
        fileTypes = (
            ("pcd files", "*.pcd"),
        )
        fileName = tk.filedialog.asksaveasfile(parent=self.root,
                                     initialdir=os.getcwd(),
                                     title="Select a file to export",
                                     filetypes=fileTypes)
        o3d.io.write_point_cloud(fileName.name, self.pointData.pointCloud)

    def exportPng(self):
        fileTypes = (
            ("png files", "*.png"),
        )
        fileName = tk.filedialog.asksaveasfile(parent=self.root,
                                     initialdir=os.getcwd(),
                                     title="Select a file to export",
                                     filetypes=fileTypes)
                        
        self.open3dVis = o3d.visualization.Visualizer() 
        visualization.visualizeAndExport(self.open3dVis, self.geometriesList, fileName)

    def exportSeparate(self):
        fileTypes = (
            ("text files", "*.txt"),
        )
        fileName = tk.filedialog.asksaveasfile(parent=self.root,
                                     initialdir=os.getcwd(),
                                     title="Name the file to export",
                                     filetypes=fileTypes)
        
        fileNameString = fileName.name
        filesList = []
        
        for i in range(len(self.pointData.classifications)):
            name = self.pointData.classifications[i].name
            f = open(fileNameString + "_%s.txt" % name, "w")
            filesList.append(f)
        
        originalLines = []
        count = 0
        with open(self.fileName, "r") as readFile:
            for line in readFile:
                if not '//' in line:
                    classificationIndex = self.pointData.labels[count] 
                    filesList[classificationIndex].write(line)
                    count += 1 
            
        for i in range(len(filesList)):
            filesList[i].close()

#Entry point to run the application
if(__name__ == "__main__"):
    app = Application()