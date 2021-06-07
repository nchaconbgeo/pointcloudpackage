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
        self.fileSelect = file_select.FileSelect(self.root, self.doneSelectingFile, closeFunction = self.root.destroy)
        # mainloop, runs infinitely
        tk.mainloop()   

    def doneSelectingFile(self):
        fileFormat = self.fileSelect.formatEntry.get()
        fileName = self.fileSelect.selectedFile
        if('.txt' in fileName):
            if(not import_export.validFormat(fileFormat)):
                messagebox.showerror("Invalid File Format", "Valid Format should contain space-separated values containing at minimum (x,y,z) values. \nInclude (r,g,b) for color, all other fields will be ignored.")
                return
            pcd = import_export.txtToPcd(fileName, fileName + "_sliced.txt", fileFormat)  
        else:
            pcd = import_export.read_point_cloud(fileName)
        originalColors = pcd.colors
        labels = np.zeros(len(pcd.points)) 
        self.pointData = PointData(fileName, pcd, labels, originalColors)
        o3d.visualization.draw_geometries([self.pointData.pointCloud])

app = Application()