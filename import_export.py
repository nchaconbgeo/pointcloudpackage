"""
Import/Export package
--------------------------
This package includes all the necessary functionality for importing / exporting point cloud data
"""

from io import TextIOWrapper


class InvalidFormatError:
    #Raised when the user specifies an
    #invalid file format
    pass


def getFormats():
    """
    :returns: list(str): list of the valid file input types
    """
    formats = ["xyzrgb_normals"]
    return formats


def write_header(writer,format):
    """
    :param writer:  TextIoWrapper obtained from running open(filename, "w")
    :param format:  String representing the format of the file being written to
    :returns: None
    """
    if not isinstance(writer, TextIOWrapper):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'w') function to obtain w")
    if not isinstance(format, str):
        raise ValueError()
    if format == "xyzrgb_normals":
        writer.write("VERSION .7\n")
        writer.write("FIELDS x y z rgb normal_x normal_y normal_z\n")
        writer.write("SIZE 4 4 4 4 4 4 4\n")
        writer.write("TYPE F F F U F F F\n")
        writer.write("COUNT 1 1 1 1 1 1 1\n")
    else:
        raise InvalidFormatError


'''
write_contents(writer, format):
writes the header for the appropriate pcd file linked to writer, using
the appropriate format. Will raise ValueError() for invalid parameters,
and InvalidFormatError for an invalid format.
'''
def write_contents(reader, writer, format):
    """
    :param reader: TextIoWrapper obtained from running open(filename, "r")
    :param writer: TextIoWrapper obtained from running open(filename, "w")
    :param format: Format of the file being written to
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