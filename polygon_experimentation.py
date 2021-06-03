"""
Visualization Package
--------------------------
This package contains functionality for visualizations and visual point cloud manipulation. 
"""

import open3d as o3d
import numpy as np
import pandas

def volume_selection(pcd, show_line_set = True, recolor_cropped_cloud = True, color_of_cropped_cloud = None):
    """
    :description: Returns a open3d.geometry.PointCloud that represents the volume selected by the user in the point selection window. This function initially opens a 
    visualizer for the user to select points to form a bounding polygon for the volume using shift + left click (the user can also use shift + right click to undo the last selected point).
    After the selection is made and the user presses 'q' to quit the current window, the function will perform calculations draw geometries in a separate visualizer as directed by the user in the arguments.  
    :param name: pcd (open3d.geometry.PointCloud)
    :param name: show_axis_aligned_bounding_box (bool)
    :param name: show_oriented_bounding_box(bool)
    :param name: show_line_set (bool)
    :param name: show_complex_hull (bool)
    :param name: recolor_cropped_cloud (bool)
    :param name: color_of_cropped_cloud 
    :param type: list
    :return: point cloud of type open3d.geometry.PointCloud representing the volume selected by the user.
    :rtype: open3d.geometry.PointCloud
    """
    
    vis = o3d.visualization.VisualizerWithEditing() 
    '''a VisualizerWithEditing() object is the first object allows us to select points to use 
    for cropping geometries and generating polygons. there are several different Visualizer() types in open3d, 
    some allow keystroke callbacks, and they all generally allow for some customization.
    '''
    vis.create_window()
    vis.add_geometry(pcd)
    print("To select vertices for your cropped volume, press shift + left click; press shift + right click to delete a selection\n")
    print("1) Press 'Y' twice to align geometry with negative direction of y-axis")
    print("2) Press 'K' to lock screen and to switch to selection mode")
    print("3) Press 'F' to switch to freeview mode")

    #Function creates a window, adds the original point cloud, and then allows user to select points given the prompt above.
    vis.run()
    vis.destroy_window()
    
    #these are the indices of the selected points that will form the polygon/volume. these indices correspond to the original point cloud
    picked = vis.get_picked_points()
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

    #adding the original point to make the drawn line set bounded. TODO: see about removing this as it is not a "true" lineset.
    indices.append([index_2, 0])
    if(linepoints):
        linepoints.append(linepoints[0])

    colorslist = [[255,0,0] for i in range(len(indices))]

    print("points gathered...\n")
    geometries = []

    #defining the volume selected by the user to use for cloud cropping/coloring and showing boxes and hulls.
    bounding_polygon = np.asarray(o3d.utility.Vector3dVector(linepoints))
    vol = o3d.visualization.SelectionPolygonVolume()
    vol.axis_max = 0
    vol.axis_min = 0
    vol.orthogonal_axis = "Z"
    vol.axis_max = np.max(bounding_polygon[:, 2])
    vol.axis_min = np.min(bounding_polygon[:, 2])
    vol.bounding_polygon = o3d.utility.Vector3dVector(bounding_polygon)
    cropped_pcd = vol.crop_point_cloud(pcd)
    uncolored_cropped_pcd = vol.crop_point_cloud(pcd)

    if(show_line_set):
        print("drawing lines....\n")
        #to define a LineSet() geometry type you need colors, points, and lines 
        lineSet = o3d.geometry.LineSet()
        lineSet.colors = o3d.utility.Vector3dVector(colorslist)
        lineSet.points = o3d.utility.Vector3dVector(linepoints)
        lineSet.lines = o3d.utility.Vector2iVector(indices)
        geometries.append(lineSet)

    if(recolor_cropped_cloud):
        if(color_of_cropped_cloud is not None):
            print("coloring selected polygon....\n")
            for i in range(len(cropped_pcd.points)):
                cropped_pcd.colors[i] = np.asarray(cropped_pcd.colors[i]) + np.asarray(color_of_cropped_cloud)
 
    geometries.append(pcd)
    geometries.append(cropped_pcd)

    #appending the original pcd such that the cropped geometry is printed with priority.
   
    o3d.visualization.draw_geometries(geometries,
                                    zoom=2,
                                    front=[5, -2, 0.5],
                                    lookat=[7.67473496, -3.24231903,  0.3062945],
                                    up=[1.0, 0.0, 0.0])

    return uncolored_cropped_pcd

def crop_volume(pcd):
    """
    :description: Returns a cropped point cloud object of type open3d.geometry.PointCloud. 
    This function opens a window for the user to select points to form a bounding polygon for the volume using shift + left click 
    (the user can also use shift + right click to undo the last selected point). This function will return a cropped Point Cloud holding all points 
    inside of the user-selected volume. 
    :param name: pcd
    :param type: open3d.geometry.PointCloud
    :return: point cloud of type open3d.geometry.PointCloud representing the volume selected by the user.
    :rtype: open3d.geometry.PointCloud
    """ 
    return volume_selection(pcd, False, False, False, False, False, None)

point_cloud = o3d.io.read_point_cloud("./sample_data/face.ply")

#Hull and cropped cloud
#ropped_pcd = volume_selection(point_cloud, False, False, False, True, True, color_of_cropped_cloud = [0.2, 0.2, .2])

#All possible geometries
# cropped_pcd = volume_selection(point_cloud, True, True, True, True, True, color_of_cropped_cloud = [0.2, 0.2, .2])

# No hull, just box and line set. 
cropped_pcd = volume_selection(point_cloud, True, True, color_of_cropped_cloud = [0.2, 0.2, .2])