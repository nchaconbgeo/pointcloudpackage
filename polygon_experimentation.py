import open3d as o3d
import numpy as np
import pandas

pcd = o3d.io.read_point_cloud("./sample_data/face.ply")
vis = o3d.visualization.VisualizerWithEditing() 
vis.create_window()
vis.add_geometry(pcd)
print("to select vertices for your polygon, press shift + left click, press shift + right click to delete a selection\n")
print("Demo for manual geometry cropping")
print("1) Press 'Y' twice to align geometry with negative direction of y-axis")
print("2) Press 'K' to lock screen and to switch to selection mode")
print("3) Drag for rectangle selection,")
print("   or use ctrl + left click for polygon selection")
print("4) Press 'C' to get a selected geometry and to save it")
print("5) Press 'F' to switch to freeview mode")
vis.run()
vis.destroy_window()

picked = vis.get_picked_points() #these are the indices of the points in the point cloud.


#preprocessing 
linepoints = []
indices = []
colorslist = []
index_1 = 0
index_2 = 1
count = 0
#TODO optimize or clean up code
for i in picked:
    linepoints.append(pcd.points[i])
    indices.append([index_1, index_2])
    count +=1
    if(count != len(picked)):
        index_1 += 1
        index_2 += 1

#TODO add testing to ensure polygon is legally formed before printing again (ie. solving crossing lines problem, zero index problems)
#we will be handling complex polygons by turning them into two polygons
print("points gathered...drawing lines....")


indices.append([index_2, 0])
linepoints.append(linepoints[0])
colorslist = [[255,0,0] for i in range(len(indices))]


bounding_polygon = np.asarray(o3d.utility.Vector3dVector(linepoints))

vol = o3d.visualization.SelectionPolygonVolume()
vol.orthogonal_axis = "Z"
print(bounding_polygon[:, 2])
vol.axis_max = np.max(bounding_polygon[:, 2])
vol.axis_min = np.min(bounding_polygon[:, 2])


lineSet = o3d.geometry.LineSet()
lineSet.colors = o3d.utility.Vector3dVector(colorslist)
lineSet.points = o3d.utility.Vector3dVector(linepoints)
lineSet.lines = o3d.utility.Vector2iVector(indices)
vol.bounding_polygon = o3d.utility.Vector3dVector(bounding_polygon)

# Crop the point cloud using the Vector3dVector
cropped_pcd = vol.crop_point_cloud(pcd)
bounding_box = cropped_pcd.get_axis_aligned_bounding_box()
bounding_box.color = (1, 0, 1)
cropped_pcd.paint_uniform_color([0,0.3,0])
# Draw the newly cropped PCD and bounding box
o3d.visualization.draw_geometries([lineSet, cropped_pcd, bounding_box],
                                  zoom=2,
                                  front=[5, -2, 0.5],
                                  lookat=[7.67473496, -3.24231903,  0.3062945],
                                  up=[1.0, 0.0, 0.0])
