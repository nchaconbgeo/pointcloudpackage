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
    visualizer.run()
    visualizer.destroy_window()
