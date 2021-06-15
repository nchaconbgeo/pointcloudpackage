import open3d as o3d
import numpy as np


def visualize(visualizer, geometries):
    """
    :Description: opens a window given an open3d.visualization.visualizer() object and a pertinent list of geometries (see open3d.geometry).
    :Returns: none
    """
    visualizer.create_window()
    for i in geometries:
        visualizer.add_geometry(i)

    options = visualizer.get_render_option()
    options.background_color = np.asarray([0.75, 0.85, 0.99])
    
    visualizer.run()
    visualizer.destroy_window()

def visualizeAndExport(visualizer, geometries, fileName):  
    """
    :description: opens up an open3d window, lets user select a view and captures an image upon quit.
    :returns: none
    """
    imageFileName = fileName.name
    visualizer.create_window()
    for i in geometries:
        visualizer.add_geometry(i)

    options = visualizer.get_render_option()
    options.background_color = np.asarray([0.75, 0.85, 0.99])
    visualizer.run()
    visualizer.capture_screen_image(filename = imageFileName) 
    visualizer.destroy_window()

def drawLines(visualizer, geometries, pcd):
    """
    :description: opens up an open3d window, lets user select points to draw a line.
    :param visualizer: visualizerWithEditing() open3d Object
    :param geometries: list of open3d geometries objects to displa.
    :param pcd: open3d point cloud objects
    :returns: indices, which represents the indices that form each line segment, and line points, which holds the list of picked points in order.
    """
    visualizer.create_window()
    for i in geometries:
        visualizer.add_geometry(i)

    options = visualizer.get_render_option()
    options.background_color = np.asarray([0.75, 0.85, 0.99])
    visualizer.run()
    visualizer.destroy_window()
    
    picked = visualizer.get_picked_points()
    linepoints = []
    indices = []
    colorslist = []
    index_1 = 0
    index_2 = 1
    count = 0
    #defining the line set between all points in a point cloud, and defining the list of the points gathered (linepoints) for the lineset and bounding polygon. 
    for i in picked:
        #to access data in a PointCloud() object, you must use the attributes (see pcd.points[i] below).
        linepoints.append(pcd.points[i])
        indices.append([index_1, index_2])
        count +=1
        if(count != len(picked)):
            index_1 += 1
            index_2 += 1

    return linepoints, indices[:-1]
  
