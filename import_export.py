"""
Import/Export package
--------------------------
This package includes all the necessary functionality for importing / exporting point cloud data
"""

from io import TextIOWrapper
import open3d as o3d
from enum import Enum

def getValidTokens():
    return ['x', 'y', 'z', 'r', 'g', 'b', 'rgb', 'nx', 'ny', 'nz']

class InvalidFormatError:
    """
    :Description: Raised when the user specifies an invalid file format
    """
    pass

def write_header(writer,format, lineCount):
    """
    :param writer:  TextIoWrapper obtained from running open(filename, "w")
    :param format:  String representing the format of the file being written to
    :returns: Dictionary (int -> str). map of the indecies of values to their types
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
    headerIndecies = {}
    for index, token in enumerate(splitFormat):
        if token in validTokens:
            if not  ('r' in token.lower() or 'g' in token.lower() or 'b' in token.lower()):
                headerIndecies[token.lower()] = 'F'
            else:
                headerIndecies[token.lower()] - 'I'
            headerIndecies.append(index)
            writer.write(token)
    writer.write('\n')
    #write byte size for each fields
    writer.write("SIZE")
    for i in range(0,len(headerIndecies)):
        writer.write(" 4")
    writer.write('\n')
    #write value types
    writer.write("TYPE")
    for key in headerIndecies.keys:
        writer.write(" " + headerIndecies[key])
    writer.write("\n")
    #write writer counts
    writer.write("COUNT")
    for i in range(0,len(headerIndecies)):
        writer.write(" 1")
    writer.write('\n')
    


def write_contents(reader, writer, format):
    """
    :description: Responsible for writing the numeric contents of the given txt file to the pcd file
    :param reader: TextIoWrapper obtained from running open(filename, "r")
    :param writer: TextIoWrapper obtained from running open(filename, "w")
    :param format: Format of the file being written to.  Can be any combination of the following tokens: \
                    x, y, z, r, g, b, rgb, Nx, Ny, Nz
    :returns: None\n
    """
    if not isinstance(writer, TextIOWrapper):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'w') function to obtain w")
    if not isinstance(format, str):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'r') function to obtain w")
    if not isinstance(reader, TextIOWrapper):
        raise ValueError()

    if format == "xyzrgb_normals":
        totalCount = 0
        missedLines = 0

        for line in reader:
            parts = line.split()
            if len(line.split()) != 9:
                #position
                output = parts[0] + " " + parts[1] + " " + parts[2] + " "
                #rgb
                output += str( int(parts[3]) * 256 ** 2 +int(parts[4]) * 256 ** 1 + int(parts[5])) + " "
                output += parts[-3] + " " + parts[-2] + " " + parts[-1]
                writer.write(output + "\n")
                totalCount += 1
            elif missedLines > 100:
                raise InvalidFormatError("File does not appear to be in specified format.  Check to ensure there are no blank lines")
            else:
                missedLines += 1
            if(totalCount % 1e6 == 0):
                print(str(totalCount) + "lines processed ")
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

def txt_to_pcd(textfile, pcdfile, inputFormat, outputFormat="xyzrgb"):
    """
    :Description: Converts the given text file to a pcd file suitible to be read in by Open3d
    :param textfile: Path to the textfile to be converted (String)
    :param pcdfile: Path where the output pcd file should be stored (String)
    :param inputFormat: The current format of the given input file (columns are assumed to be space separated)
    :outputFormat: The desired output format of the given pcd file (Defaults to xyzrgb)
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

    write_header(write_header, format)

    write_contents(reader, writer, lineCount)

    reader.close()
    writer.close()



    
