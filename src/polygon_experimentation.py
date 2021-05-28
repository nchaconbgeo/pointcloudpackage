import open3d as o3d
import numpy as np
import pandas

def volume_selection(pcd, show_axis_aligned_bounding_box = True, show_oriented_bounding_box = True, show_line_set = True, show_complex_hull = True, recolor_cropped_cloud = True, color_of_cropped_cloud = None):
    """
    Returns a open3d.geometry.PointCloud that represents the volume selected by the user in the point selection window. This function initially opens a 
    visualizer for the user to select points to form a bounding polygon for the volume using shift + left click (the user can also use shift + right click to undo the last selected point).
    After the selection is made and the user presses 'q' to quit the current window, the function will perform calculations draw geometries in a separate visualizer as directed by the user in the arguments.  
    :param name: pcd
    :param type: open3d.geometry.PointCloud
    :param name: show_axis_aligned_bounding_box
    :param type: bool
    :param name: show_oriented_bounding_box
    :param type: bool
    :param name: show_line_set
    :param type: bool
    :param name: show_complex_hull
    :param type: bool
    :param name: recolor_cropped_cloud
    :param type: bool
    :param name: color_of_cropped_cloud 
    :param type: list
    :return: point cloud of type open3d.geometry.PointCloud representing the volume selected by the user.
    :rtype: open3d.geometry.PointCloud
    """

    vis = o3d.visualization.VisualizerWithEditing() 
    vis.create_window()
    vis.add_geometry(pcd)
    print("To select vertices for your cropped volume, press shift + left click; press shift + right click to delete a selection\n")
    print("1) Press 'Y' twice to align geometry with negative direction of y-axis")
    print("2) Press 'K' to lock screen and to switch to selection mode")
    print("3) Press 'F' to switch to freeview mode")
    vis.run()
    vis.destroy_window()

    picked = vis.get_picked_points() #these are the indices of the points in the point cloud.
    linepoints = []
    indices = []
    colorslist = []
    index_1 = 0
    index_2 = 1
    count = 0

    for i in picked:
        linepoints.append(pcd.points[i])
        indices.append([index_1, index_2])
        count +=1
        if(count != len(picked)):
            index_1 += 1
            index_2 += 1
    indices.append([index_2, 0])
    linepoints.append(linepoints[0])
    colorslist = [[255,0,0] for i in range(len(indices))]
   
    #TODO add testing to ensure polygon is legally formed before printing again (ie. solving crossing lines problem, zero index problems)
    #we will be handling complex polygons by turning them into two polygons

    print("points gathered...\n")
    geometries = []
    bounding_polygon = np.asarray(o3d.utility.Vector3dVector(linepoints))
    vol = o3d.visualization.SelectionPolygonVolume()
    vol.orthogonal_axis = "Z"
    vol.axis_max = np.max(bounding_polygon[:, 2])
    vol.axis_min = np.min(bounding_polygon[:, 2])
    vol.bounding_polygon = o3d.utility.Vector3dVector(bounding_polygon)
    cropped_pcd = vol.crop_point_cloud(pcd)
    uncolored_cropped_pcd = vol.crop_point_cloud(pcd)

    if(show_line_set):
        print("drawing lines....\n")
        lineSet = o3d.geometry.LineSet()
        lineSet.colors = o3d.utility.Vector3dVector(colorslist)
        lineSet.points = o3d.utility.Vector3dVector(linepoints)
        lineSet.lines = o3d.utility.Vector2iVector(indices)
        geometries.append(lineSet)

    #if we are passing a croupped 
    if(recolor_cropped_cloud):
        if(color_of_cropped_cloud is not None):
            print("coloring selected polygon....\n")
            for i in range(len(cropped_pcd.points)):
                cropped_pcd.colors[i] = np.asarray(cropped_pcd.colors[i]) + np.asarray(color_of_cropped_cloud)
    
    geometries.append(cropped_pcd)

    if(show_axis_aligned_bounding_box):
        print("drawing axis-aligned bounding box....\n")
        axis_aligned_bounding_box = cropped_pcd.get_axis_aligned_bounding_box()
        axis_aligned_bounding_box.color = (1, 0, 1)
        geometries.append(axis_aligned_bounding_box)

    if(show_oriented_bounding_box):
        print("drawing oriented bounding box....\n")
        obb = cropped_pcd.get_oriented_bounding_box()
        obb.color = (0, 1, 1)

    if(show_complex_hull):
        print("creating complex hull....\n")
        hull, _ = cropped_pcd.compute_convex_hull()
        hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
        hull_ls.paint_uniform_color((0.5, 1, 0.5))
        geometries.append(hull_ls)

    geometries.append(pcd)

    o3d.visualization.draw_geometries(geometries,
                                    zoom=2,
                                    front=[5, -2, 0.5],
                                    lookat=[7.67473496, -3.24231903,  0.3062945],
                                    up=[1.0, 0.0, 0.0])

    return uncolored_cropped_pcd

def crop_volume(pcd):
    """
    Returns a cropped point cloud object of type open3d.geometry.PointCloud. 
    This function opens a window for the user to select points to form a bounding polygon for the volume using shift + left click 
    (the user can also use shift + right click to undo the last selected point). This function will return a cropped Point Cloud holding all points 
    inside of the user-selected volume. 
    :param name: pcd
    :param type: open3d.geometry.PointCloud
    :return: point cloud of type open3d.geometry.PointCloud representing the volume selected by the user.
    :rtype: open3d.geometry.PointCloud
    """ 
    return volume_selection(pcd, False, False, False, False, False, None)

point_cloud = o3d.io.read_point_cloud("../sample_data/face.ply")
cropped_pcd = volume_selection(point_cloud, False, False, False, True, True, color_of_cropped_cloud = [0.2, 0.2, .2])
# cropped_pcd = volume_selection(point_cloud, True, True, True, True, True, color_of_cropped_cloud = [0.2, 0.2, .2])
# cropped_pcd = volume_selection(point_cloud, True, True, True, True, False, color_of_cropped_cloud = [0.2, 0.2, .2])