import open3d as o3d
import numpy as np
from import_export import * 

format = "x y z r g b alpha nx ny nz"
print("initiating file processesing")
txt_to_pcd("C:/Users/specs/Open3D_PC/Mudstone.txt", "C:/Users/specs/Open3D_PC/Mudstone1.pcd", format)
print("finished importing file")

pcd = get_pcd("C:/Users/specs/Open3D_PC/Mudstone1.pcd")
original_colors = []
original_colors = pcd.colors
labels = np.zeros(len(pcd.points))



o3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[27.98049927, -68.83489990, 1309.67395020],
                                  up=[-0.0694, -0.9768, 0.2024])