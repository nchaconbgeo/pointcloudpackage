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
