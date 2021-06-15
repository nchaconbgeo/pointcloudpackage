import open3d as o3d



def downSampleFile(input_name, output_name, voxel_size):
    """
    :Description: Takes a pcd file, and creates a downsized version of the file using voexel down smapling
    :param input_name: name of the input pcd file
    :param output_name: name of the output pcd file to be created
    :Raises: Value error
    """
    if not ".pcd" in input_name:
        raise ValueError("Invalid file type.  Please ensure your output file is of type pcd (ensure file extension is in name)")
    pcd = o3d.io.read_point_cloud(input_name)
    downsampled = pcd.voxel_down_sample(voxel_size)
    o3d.io.write_point_cloud(output_name, downsampled, write_ascii=True, )

