from GUI import Classification
from GUI.Classification import classification
import open3d as o3d
import numpy as np

class PointData:
    """
    :Description: Container class for open3d point cloud, per-point classification data, and classification types
    """
    fileName = ""
    pointCloud = None
    hashMap = {}
    labels = None
    originalColors = None
    classifications = None
    selectedIndex = 0    #index of selected label

    def __init__(self, fileName, pointCloud, labels, originalColors):
        self.fileName = fileName
        self.pointCloud = pointCloud 
        self.labels = labels
        self.originalColors = originalColors
        self.classifications = [classification.Classification(color = '#ffffff')]
        for i, point in enumerate(pointCloud.points):
            tup = (point[0], point[1], point[2])
            self.hashMap[tup] = i
        

    def processLabels(self, visualizer, classificationIndex):
        """
        :description:
        :param visualizer: visualizer of type open3d.visualization.visualizerWithEditing()
        :param selectedClassification: 
        """

        #Open3D VisualizerwithEditing()
        #volume selection - math or open3d bounding polygon case
        #assign colors and labels to points within volume selection

        picked = visualizer.get_picked_points()
        pickedPointsIndices = []


        if(len(picked) < 4): #4 points needed to create a convex hull
            return

        #defining the list of the points gathered (linepoints) for the lineset and bounding polygon. 
        for i in picked:
            #to access data in a PointCloud() object, you must use the attributes (see pcd.points[i] below).
            pickedPointsIndices.append(self.pointCloud.points[i])

        pickedPointsIndices.append(pickedPointsIndices[0]) 
        boundingPolygon = np.asarray(o3d.utility.Vector3dVector(pickedPointsIndices))
        vol = o3d.visualization.SelectionPolygonVolume()
        vol.axis_max = 0
        vol.axis_min = 0
        vol.orthogonal_axis = "Z"
        vol.axis_max = np.max(boundingPolygon[:, 2])
        vol.axis_min = np.min(boundingPolygon[:, 2])
        vol.bounding_polygon = o3d.utility.Vector3dVector(boundingPolygon)
        #cropped_pcd 
        croppedPcd = vol.crop_point_cloud(self.pointCloud)
 
        cloudColor = self.classifications[classificationIndex].color
        
        floatArray = tuple(float(int(cloudColor[i:i+2], 16)) / 255 for i in (1, 3, 5))
        rgbArray = np.asarray(floatArray)

        for point in croppedPcd.points:
            tup = (point[0], point[1], point[2])
            index = self.hashMap[tup]
            if(classificationIndex == 0):
                self.pointCloud.colors[index] = self.originalColors[index]
            else:
                self.pointCloud.colors[index] = self.colorTransform(self.originalColors[index], rgbArray)
            
            self.labels[index] = classificationIndex
    

    def processColorChange(self):
        """
        :description: When the user changes the color of a class, it runs through every point and recalculates the color.
        :Returns: none
        """
        print("Processing color")
        for i in range(len(self.pointCloud.points)):
            labelIndex = self.labels[i]
            if(labelIndex != 0):
                originalColor = self.originalColors[i]
                classificationColor = self.classifications[labelIndex].rgbColor
                self.pointCloud.colors[i] = self.colorTransform(originalColor, classificationColor)
               
    def colorTransform(self, originalColor, classificationColor):
        """
        :description: Helper function for changing the color -- defines how much texture should be retained
        :param originalColor: the original color of a given point
        :param classificationColor: the color selected by the user in which the point will be changed to.
        :Returns: none
        """
        outputColor = originalColor * 0.4 + classificationColor * (1-0.4)
        return outputColor


        




