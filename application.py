import tkinter as tk
from GUI import file_select
import import_export
import numpy as np
import open3d as o3d
from point_data import PointData
from tkinter import messagebox

class Application:
    root = None
    pointData = None
    fileSelect = None


    def __init__(self):
        # creates a Tk() object
        self.root = tk.Tk()
        self.root.withdraw()
        self.fileSelect = file_select.FileSelect(self.root, self.doneSelectingFile, closeFunction = self.closeApp)
        # mainloop, runs infinitely
        tk.mainloop()   

    def doneSelectingFile(self):
        fileFormat = self.fileSelect.formatEntry.get().lower()
        fileName = self.fileSelect.selectedFile
        self.pointData = import_export.readData(fileName, fileFormat)

        self.fileSelect.frame.destroy()
        o3d.visualization.draw_geometries([self.pointData.pointCloud])

    def closeApp(self):
        self.root.destroy()
        
app = Application()