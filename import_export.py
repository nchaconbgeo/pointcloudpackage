
"""
Import/Export package
--------------------------
This package includes all the necessary functionality for importing / exporting point cloud data
"""

from io import TextIOWrapper
import open3d as o3d
from enum import Enum
import numpy as np
from point_data import PointData
from tkinter import messagebox



class InvalidFormatError:
    """
    :Description: Raised when the user specifies an invalid file format
    """
    pass

class InputFormat(Enum):
    XYZ = 1
    XYZ_R_G_B = 2
    XYZ_RGB = 3


def validFormat(format):
    """
    :Description: Checks if x, y, and z are elements in the fields for parsing. Checks if any 'r' 'g' or 'b' elements are in the format then all 'rgb' values are in format.
    :param format: format of the file passed in
    :Returns: boolean value
    """
    fields = format.lower().split()
    if not('r' in fields and 'g' in fields and 'b' in fields) and ('r' in fields or 'g' in fields or 'b' in fields):
        return False
    else:
        return ('x' in fields and 'y' in fields and 'z' in fields)
    

def readData(fileName, fileFormat):
    """
    :Description: wrapper function to process all data and returns pointData object.
    :param fileName: name of the file for import of type .pcd, .ply, .txt
    :param fileFormat: specifies data organization in the file (typically 'xyz' or 'xyzrgb').
    :Returns: pointData() object.
    """
    pcd = None
    if('xyzrgb' in fileName):
        pcd = readPointCloud(fileName, fileFormat="xyzrgb")
    elif('xyz' in fileName):
        pcd = readPointCloud(fileName, fileFormat="xyz")
    elif('.txt' in fileName):
        #Checks file format to make sure it is valid with xyz or xyzrgb
        if(not validFormat(fileFormat)):
            messagebox.showerror("Invalid File Format", "Valid Format should contain space-separated values containing at minimum (x,y,z) values. \nInclude a complete set of (r,g,b) values for color; all other fields will be ignored.")
            return
        #Renames file when creating sliced file. 
        newFile = fileName.replace(".txt", "." + fileFormat.lower())
        newFile = newFile.replace(" ", "")
        pcd = txtToPcd(fileName, newFile, fileFormat)  
    else:
        pcd = readPointCloud(fileName)
    originalColors = pcd.colors
    labels = np.zeros(len(pcd.points)) 
    pointData = PointData(fileName, pcd, labels, originalColors)
    return pointData



#return indices [x, y, z], [x, y, z, rgb] or [x, y, z, r, g, b], and the format
def parseFormat(format):
    locations = format.lower().split()
    x_location = locations.index('x')
    y_location = locations.index('y')
    z_location = locations.index('z')
    
    #location of data in each line
    r_location = None
    g_location = None
    b_location = None
    rgb_location = None

    colorFormat = None

    
    try:
        #if any locations are not found throw an exception that skips settings the color format
        r_location = locations.index('r')
        g_location = locations.index('g')
        b_location = locations.index('b')
        colorFormat = 'r_g_b'
    except:
        pass
    try:
        #if rgb location not found throw an exception that skips settings the color format
        rgb_location = locations.find('rgb')
        colorFormat = 'rgb'
    except:
        pass

    #return the correct format based on given color data
    if colorFormat == None:
        return ([x_location, y_location, z_location], InputFormat.XYZ)
    if colorFormat == 'rgb':
        return ([x_location, y_location, z_location, rgb_location], InputFormat.XYZ_RGB)
    if colorFormat == 'r_g_b':
        return ([x_location, y_location, z_location, r_location, g_location, b_location], InputFormat.XYZ_R_G_B)


def writeContents(reader, writer, indices, inputFormat):
    """
    :description: Responsible for writing the numeric contents of the given txt file to the pcd file
    :param reader: TextIoWrapper obtained from running open(filename, "r")
    :param writer: TextIoWrapper obtained from running open(filename, "w")
    :param format: Dictionary of format tokens to indices.
    :returns: None\n
    """

    if not isinstance(writer, TextIOWrapper):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'w') function to obtain writer")
    if not isinstance(inputFormat, InputFormat):
        raise ValueError("Input Format is expected to be of type InputFormat.")
    if not isinstance(reader, TextIOWrapper):
        raise ValueError("reader must be of type TextIOWrapper.\n Use the open(filename, 'r') function to obtain writer")

    outputCount = len(indices)

    totalCount = 0
    missedLines = 0

    for line in reader:
        if len(line) == 0 or (len(line) >= 2 and line[0] == '/' and line [1] == '/') or (len(line) >= 1 and line[0] == '#'):
            print("Comment found: " + line)
            continue #comment found
        fields = line.split()
        
        x = fields[indices[0]]
        y = fields[indices[1]]
        z = fields[indices[2]]

        if(inputFormat == InputFormat.XYZ):
            writer.write(str(x) + " " + str(y) + " " + str(z)) #x y and z locations are stored in indices
            outputCount += 1
            continue

        r = 0
        g = 0
        b = 0
        if(inputFormat == InputFormat.XYZ_RGB):
            rgb = fields[indices[3]]
            r = int(int(rgb) / (256 ** 2)) % 256
            g = int(int(rgb) / (256 ** 1)) % 256
            b = int(int(rgb) / (256 ** 0)) % 256
        
        if(inputFormat == InputFormat.XYZ_R_G_B):
            r = int(fields[indices[3]])
            g = int(fields[indices[4]])
            b = int(fields[indices[5]])
            
        outputCount += 1
        output = str(x) + " " + str(y) + " " + str(z) + " " + str(r / 255) + " " + str(g / 255) + " " + str(b / 255)  
        writer.write(output + "\n")
    return outputCount

def getPcd(pcdFile):
    """
    :param pcdFile: Path to the pcdfile to create a pcd object of.
    :returns: pcd object that can be used for open3d visualization
    :Raises: ValueError: If file does not contain appropriate extension
    """
    if not ".pcd" in pcdFile[-4:]:
        raise ValueError("Invalid file.  Check to ensure your file ends in .pcd")

    return o3d.io.read_point_cloud(pcdFile)

def txtToPcd(textfile, pcdfile, inputFormat):
    """
    :Description: Converts the given text file to a pcd file suitible to be read in by Open3d
    :param textfile: Path to the textfile to be converted (String)
    :param pcdfile: Path where the output pcd file should be stored (String)
    :param inputFormat: Format of the file being read from (str).  Can be any combination of the following tokens: \
                    x, y, z, r, g, b, rgb, Nx, Ny, Nz
    :Returns: None
    :Raises: ValueError
    """
    if not '.' in textfile or not isinstance(textfile, str):
        raise ValueError("Invalid path.  Please ensure your file has the .txt extension")
    
    if not ".txt" in pcdfile:   # append appropriate extension if not present
        pcdfile = pcdfile + ".txt"
    
    reader = open(textfile, "r")

    lineCount = 0
    for line in reader:
        line = line.strip() #remove trailing and preceding whitespace
        if (len(line) == 0 or len(line) >= 2 and line[0] == '/' and line [1] == '/') or (len(line) >= 1 and line[0] == '#'):
            continue #comment found
        lineCount += 1
    reader.close()

    reader = open(textfile, "r")
    writer = open(pcdfile, "w+")
    
    format = parseFormat(inputFormat)
    indices = format[0]
    inputType = format[1]
    
    writeContents(reader, writer, indices, inputType)

    reader.close()
    writer.close()

    stringRepresentation = {InputFormat.XYZ: 'xyz', InputFormat.XYZ_R_G_B: "xyzrgb"}[inputType] #return order of data (xyz or xyzrgb)
    pcd = readPointCloud(pcdfile, stringRepresentation)
    return pcd 

def readPointCloud(fileName, fileFormat = None):
    """
    :Description: Wrapper function to manage open3d's import functionality.
    :param filename: name of the file for import
    :param fileFormat: format of the file (ie. 'xyz')
    :Returns: open3d.geometry.PointCloud() object.
    """
    if(fileFormat != None):
        return o3d.io.read_point_cloud(fileName, format = fileFormat)
    else:
        return o3d.io.read_point_cloud(fileName)