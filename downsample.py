import open3d as o3d



def downSampleFile(input_name, output_name, voxel_size):
    pcd = o3d.io.read_point_cloud(input_name)
    downsampled = pcd.voxel_down_sample(voxel_size)
    o3d.io.write_point_cloud(output_name, downsampled, write_ascii=True, )

