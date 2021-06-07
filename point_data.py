import open3d as o3d
import numpy as np

class PointData:
    fileName = ""
    pointCloud = None
    labels = None
    originalColors = None

    def __init__(self, fileName, pointCloud, labels, originalColors):
        self.fileName = fileName
        self.pointCloud = pointCloud 
        self.labels = labels
        self.originalColors = originalColors




