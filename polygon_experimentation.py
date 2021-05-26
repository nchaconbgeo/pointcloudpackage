import open3d as o3d
import numpy as np
import pandas

pcd = o3d.io.read_point_cloud("sample_data/face.ply")
vis = o3d.visualization.VisualizerWithEditing() 
vis.create_window()
vis.add_geometry(pcd)
print("to select vertices for your polygon, press shift + left click, press shift + right click to delete a selection\n")
vis.run()
vis.destroy_window()
print("points gathered...drawing lines....")

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

indices.append([index_2, 0])
linepoints.append(linepoints[0])
colorslist = [[255,0,0] for i in range(len(indices))]
print(indices)
print(linepoints)


lineSet = o3d.geometry.LineSet()
lineSet.colors = o3d.utility.Vector3dVector(colorslist)
lineSet.points = o3d.utility.Vector3dVector(linepoints)
lineSet.lines = o3d.utility.Vector2iVector(indices)
o3d.visualization.draw_geometries([pcd, lineSet])

