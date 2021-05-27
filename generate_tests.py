import random
import time

'''
Generates random pointcloud data in the [x y z r g b nx ny nz] format
output_filename -> name of the file to output data to
n_lines -> number of points in the file
'''
def generate_float(greaterThanOne = True):
    random.seed(random.randint(0,1000000))
    x = random.random()
    x = "{:.8f}".format(x)
    x = float(x)
        
    if greaterThanOne:
        x += random.randint(-1000, 1000)
    elif x % 2 == 0:
        x = x * -1.0
    return x

def generate_rgb():
    random.seed(time.time())
    return random.randint(0, 255)

def generate_xyzrgb_normals(output_filename, n_lines):
    w = open(output_filename, "w+")
    for i in range(0, n_lines):
        output = str(generate_float()) + " " + str(generate_float()) + " " + str(generate_float()) + " "
        output += str(generate_rgb()) + " " + str(generate_rgb()) + " " + str(generate_rgb()) + " "
        output += str(generate_float()) + " " + str(generate_float()) + " " + str(generate_float()) + "\n"
        w.write(output)
    w.close()

generate_xyzrgb_normals("tests/import/input_1_xyzrgb_normals.txt", 1)
print("finished input_1_xyzrgb_normals")
generate_xyzrgb_normals("tests/import/input_10_xyzrgb_normals.txt", 10)
print("finished input_10_xyzrgb_normals")
generate_xyzrgb_normals("tests/import/input_100_xyzrgb_normals.txt", 100)
print("finished input_100_xyzrgb_normals")
generate_xyzrgb_normals("tests/import/input_85_xyzrgb_normals.txt", 85)
print("finished input_85_xyzrgb_normals")
generate_xyzrgb_normals("tests/import/input_76_xyzrgb_normals.txt", 76)
print("finished input_76_xyzrgb_normals")