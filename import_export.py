"""
Import/Export package
--------------------------
This package includes all the necessary functionality for importing / exporting point cloud data
"""

from io import TextIOWrapper
import open3d as o3d
from enum import Enum

def getValidTokens():
    """
    :Returns: List of strings representing the valid tokens for file input
    """
    return ['x', 'y', 'z', 'r', 'g', 'b', 'rgb', 'normal_x', 'normal_y', 'normal_z']

class InvalidFormatError:
    """
    :Description: Raised when the user specifies an invalid file format
    """
    pass

def write_header(writer, format, lineCount):
    """
    :param writer:  TextIoWrapper obtained from running open(filename, "w")
    :param format:  String representing the format of the file being written to
    :returns: dict() of tokens mapped with indices
    """
    if not isinstance(writer, TextIOWrapper):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'w') function to obtain w")
    if not isinstance(format, str):
        raise ValueError()
    writer.write("VERSION .7\n")

    #Write fields
    writer.write("FIELDS ")
    splitFormat = format.split()
    validTokens = getValidTokens()
    tokenToIndex = {}       #maps the token to the index at which it is found
    typeContents = ""
    appendToEnd = False
    for index, token in enumerate(splitFormat):
        token = token.lower()
        if token in validTokens:
            tokenToIndex[token] = index
            if token == 'r' or token == 'g' or token == 'b':
                appendToEnd = True
            elif token == "rgb":
                if index == 0:
                    typeContents += "U"
                else:
                    typeContents += " U"
            else:
                if index == 0:
                    typeContents = "F"
                    writer.write(token)
                else:
                    typeContents += " F"
                    writer.write(" " + token)
    if appendToEnd:
        typeContents += " U"
        writer.write(" rgb")
            
    writer.write('\n')
    #write byte size for each fields
    writer.write("SIZE")
    for i in range(0,len(typeContents.split())):
        writer.write(" 4")
    writer.write('\n')
    #write value types
    writer.write("TYPE ")
    writer.write(typeContents + '\n')
    #write field counts
    writer.write("COUNT")
    for i in range(0,len(typeContents.split())):
        writer.write(" 1")
    writer.write('\n')
    #write width
    writer.write("WIDTH " + str(lineCount) + '\n')
    writer.write("HEIGHT 1\n")

    writer.write("VIEWPOINT 0 0 0 1 0 0 0\n")

    writer.write("POINTS " + str(lineCount) + '\n')

    writer.write("DATA ascii\n")

    return tokenToIndex
    


def write_contents(reader, writer, format):
    """
    :description: Responsible for writing the numeric contents of the given txt file to the pcd file
    :param reader: TextIoWrapper obtained from running open(filename, "r")
    :param writer: TextIoWrapper obtained from running open(filename, "w")
    :param format: Dictionary of format tokens to indices.
    :returns: None\n
    """
    if not isinstance(writer, TextIOWrapper):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'w') function to obtain writer")
    if not isinstance(format, dict):
        raise ValueError("Format is expected to be of type dict.")
    if not isinstance(reader, TextIOWrapper):
        raise ValueError("reader must be of type TextIOWrapper.\n Use the open(filename, 'r') function to obtain writer")

    totalCount = 0
    missedLines = 0

    for line in reader:
        parts = line.split()
        rgbVals = [-1, -1, -1]
        if len(parts) < len(format) and missedLines > 100:
            raise InvalidFormatError("File does not match format provided")
        elif len(parts) < len(format):
            missedLines += 1
            continue
        for index, token in enumerate(format.keys()):
            if token == 'r':
                rgbVals[0] = int(parts[format[token]])
            elif token == 'g':
                rgbVals[1] = int(parts[format[token]])
            elif token == 'b':
                rgbVals[2] = int(parts[format[token]])

            if not (token == "r" or token =="g" or token == "b"):
                if index == 0:
                    writer.write(parts[format[token]])
                else:
                    writer.write(" " + parts[format[token]])
        #check to ensure all r, g, and b values are present
        if rgbVals[0] == -1:
            rgbVals[0] = 0
        if rgbVals[1] == -1:
            rgbVals[1] = 0
        if rgbVals[2] == -1:
            rgbVals[2] = 0
        #calculate singular rgb value if relevant
        if not (rgbVals[0] == 0 and rgbVals[1] == 0 and rgbVals[2] == 0):
            writer.write(' ' + str( rgbVals[0] * 256 ** 2 + rgbVals[1] * 256 ** 1 + rgbVals[2]))
        
        writer.write('\n')
        totalCount += 1
        if(totalCount % 1e6 == 0):
            print(str(totalCount) + " lines processed ")
    return

def get_pcd(pcdFile):
    """
    :param pcdFile: Path to the pcdfile to create a pcd object of.
    :returns: pcd object that can be used for open3d visualization
    :Raises: ValueError: If file does not contain appropriate extension
    """
    if not ".pcd" in pcdFile:
        raise ValueError("Invalid file.  Check to ensure your file ends in .pcd")

    return o3d.io.read_point_cloud(pcdFile)

def txt_to_pcd(textfile, pcdfile, inputFormat):
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
    
    if not ".pcd" in pcdfile:   # append appropriate extension if not present
        pcdfile = pcdfile + ".pcd"
    
    reader = open(textfile, "r")

    lineCount = 0
    for line in reader:
        lineCount += 1
    reader.close()

    reader = open(textfile, "r")
    writer = open(pcdfile, "w+")

    indexList = write_header(writer, inputFormat, lineCount)

    write_contents(reader, writer, indexList)

    reader.close()
    writer.close()
