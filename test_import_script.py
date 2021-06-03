from import_export import *
import open3d as o3d

# txt_to_pcd("sample_data/Mudstone.txt", "sample_data/Mudstone.pcd", "xyzrgb_normals")
pcd = get_pcd("sample_data/Mudstone.pcd")

print(pcd)

o3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[27.98049927, -68.83489990, 1309.67395020],
                                  up=[-0.0694, -0.9768, 0.2024])