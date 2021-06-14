import open3d as o3d
import numpy as np
import matplotlib as plt
from PIL import Image

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

def visualizeAndExport(visualizer, geometries, fileName):  
    """
    :description: opens up an open3d window, lets user select a view and captures an image upon quit.
    :returns: none
    """
    imageFileName = fileName.name
    visualizer.create_window()
    for i in geometries:
        visualizer.add_geometry(i)

    options = visualizer.get_render_option()
    options.background_color = np.asarray([0.75, 0.85, 0.99])
    visualizer.run()
    visualizer.capture_screen_image(filename = imageFileName) 
    visualizer.destroy_window()
