"""
Import/Export package
--------------------------
This package includes all the necessary functionality for importing / exporting pointcloud data
"""

from io import TextIOWrapper


class InvalidFormatError:
    #Raised when the user specifies an
    #invalid file format
    pass

formats = ["xyzrgb_normals"]


'''
write_header(writer, format):
writes the header for the appropriate pcd file linked to writer, using
the appropriate format. Will raise ValueError() for invalid parameters,
and InvalidFormatError for an invalid format.

writer: TextIoWrapper obtained from running open(filename, "w")
format: String that matches the format of the input file
'''
def write_header(writer,format):
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
    if not isinstance(writer, TextIOWrapper):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'w') function to obtain w")
    if not isinstance(format, str):
        raise ValueError("writer must be of type TextIOWrapper.\n Use the open(filename, 'r') function to obtain w")
    if not isinstance(reader, TextIOWrapper):
        raise ValueError()
    if format == "xyzrgb_normals":
        totalCount = 0
        missedLines = 0
        parts = line.split()
        for line in r:
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
                print(str(totalCount) + "/" + str(lineCount) + " processed (" + "{:.1f}".format(100 * totalCount / lineCount) + "%)")
    return

'''
Parses an input text file into an appropriate pcd for viewing.
filename -> name of the input text file
output_filename -> name of the output pcd file
format -> the format of the input text file

Appropriate formats include:
xyz
xyz_normals
xyzrgb
xyzrgb_normals
'''
def parseInput(filename, output_filename="", format="xyzrgb_normals"):
    if not format in formats:
         raise InvalidFormatError
    name = filename.split(".")[0]
    extension = filename.split(".")[1]
    if len(output_filename == 0):
        output_filename = "/tests/import" + name + "_sliced." + extension
    elif not '.' in output_filename:
        output_filename = output_filename + "." + extension
    
    r = open(filename, 'r')
    lineCount = 0

    for line in r:
        lineCount += 1
        if(lineCount % 1e6 == 0):
            print("Counted " + str(lineCount) + " lines")
    r.close()

    r = open(filename, "r")

    w = open(output_filename, "w")

    write_header(w, format)
    write_contents(w, format)
    w.close()
    print("Finished outputting to " + output_filename)



#ORIGINAL CODE v v v 
'''
include_normals = True

r = open(filename, "r")
lineCount = 0
for line in r:
    lineCount += 1
    if(lineCount % 1e6 == 0):
        print("Counted " + str(lineCount) + " lines")
print("Counted " + str(lineCount) + " lines")

r.close()

r = open(filename, "r")

w = open(output_filename, "w")

w.write("VERSION .7\n")
if(include_normals):
    w.write("FIELDS x y z rgb normal_x normal_y normal_z\n")
    w.write("SIZE 4 4 4 4 4 4 4\n")
    w.write("TYPE F F F U F F F\n")
    w.write("COUNT 1 1 1 1 1 1 1\n")

else:    
    w.write("FIELDS x y z rgb\n")
    w.write("SIZE 4 4 4 4\n")
    w.write("TYPE F F F U\n")
    w.write("COUNT 1 1 1 1\n")

w.write("WIDTH " + str(lineCount) + "\n")
w.write("HEIGHT 1\n")
w.write("VIEWPOINT 0 0 0 1 0 0 0\n")
w.write("POINTS " + str(lineCount) + "\n") 
w.write("DATA ascii\n")

totalCount = 0

for line in r:
    parts = line.split()
    if(len(parts) < 3):
        print("blank line at " + str(totalCount) + "/" + str(lineCount))
        print("Line contents: " + line)
        continue
    if(line[0] == "/" and line[1] == "/"):
        print("Comment found:", line)
        continue

    
    #position
    output = parts[0] + " " + parts[1] + " " + parts[2] + " "
    #rgb
    output += str( int(parts[3]) * 256 ** 2 +int(parts[4]) * 256 ** 1 + int(parts[5])) + " "

    output += parts[-3] + " " + parts[-2] + " " + parts[-1]
    
    w.write(output + "\n")
    
    totalCount += 1
    if(totalCount % 1e6 == 0):
        print(str(totalCount) + "/" + str(lineCount) + " processed (" + "{:.1f}".format(100 * totalCount / lineCount) + "%)")
    
w.close()
print(str(totalCount) + "/" + str(lineCount) + " processed (" + "{:.1f}".format(100 * totalCount / lineCount) + "%)")
print("Finished outputting to " + output_filename)
'''
