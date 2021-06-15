import tkinter as tk
import numpy as np

class Classification:
    """
    :Description: Container class for storing classification info
    """

    classificationID = 0
    classificationCount = 0

    color = ''   #default color = obnoxious magenta
    name = ''
    description = ''
    rgbColor = None

    def __init__(self, name = 'Unclassified', description = 'Default Classification description', color = '#ffffff'):
        """
        :Description: Fill classification container's information.
        :param color: color in hex format. the classification will be randomly assigned a color if no color is provided.
        :return: Classification
        """
        self.classificationID = Classification.classificationCount
        Classification.classificationCount += 1
        self.name = name
        self.description = description
        self.setColor(color)

    def __str__(self):
        """
        :Description: convert classification to a string
        """ 
        return str(self.name) + ": " + str(self.description) + ", color: " + self.color

    def setColor(self, hexColor):
        """
        :Description: convert hex color from tkinter interface to an rgb float array and setting the current hex value.
        """ 
        self.color = hexColor
        floatArray = tuple(float(int(self.color[i:i+2], 16)) / 255 for i in (1, 3, 5))
        self.rgbColor = np.asarray(floatArray)
