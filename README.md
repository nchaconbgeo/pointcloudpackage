# GeoPointClouds 3D Visualization Software

GeoPointClouds is a 3D Visualization Software created to perform geological interpretations on point cloud data. Version 0.0 functionality consists of:
  * File Input and Output for Point Cloud Data Types: .txt<sup> 1</sup>, .ply, .pcd, .pts
  * Graphical Visualization of 3d Point Clouds:
    * Ability to rotate and perform zoom and cropping operations on data  
  * Volume Selection for Point Cloud Labeling:
    * Polygon Selection
    * Projection Selection
  * Line drawing functionality
  * Graphical User Interface

All functionality is contained within an application that can be run as an executable on MacOS and Windows. To install the software, see [installation](#installation). This application requires Python version >3.8 to run.

<sup>1</sup> User must specify format for .txt files in the [File Import Menu](#file-import-menu) 

## Basic App Navigation

### File Import Menu
upon launching the application, you will be see an import file menu to load your file in for use. The components of this menu consist of:
  * a `select file` button: this will launch your file explorer to locate the point cloud file. 
  * a `file format` entry box: if you are using a .txt file, this is where you will define the file heading format, such as 'x y z r g b' or 'x y z r g b nx ny nz'
  * a `done` button: click to begin processing your point cloud file for the program. 
![Image of File Import Menu](https://github.com/nchaconbgeo/pointcloudpackage/blob/880882d4609b8b2aa132f7eb7d34bdbd2db4bf9d/R3dF8LChjjVPzA0pDqUXoSYy9t1eK2RRW5jquabGel_H5_XPiKdv2jDJfidlsbG88s8_LCcRUvSiqM7aY-i3iiDwUG50hAhSVn_FPrI4dMeyWPMZ6fCetf_L04XTLexrpRpJEQNS_vo(1).png)

*Pro Tip:* when importing a .txt file and providing a format (ie. a txt file named pointcloud.txt with format 'x y z r g b'), GeoPointClouds will automatically generate a new file for your data with the extension of its format, such as 'pointcloud.xyzrgb.txt'. This file will generally be smaller and optimized for the program, and you can use it in the future without supplying the format since the format is specified in the extension. 

### Main Menu:
after importing a file for use in GeoPointClouds, you will be directed to the main menu. The main menu has the following functionalities:
  * `Select Volume`: see [Select Volume](#select-volume)
  * `Edit/View Labels`: see [Edit/View Labels](#editview-labels)
  * `Draw Line`: see [Draw Line](#draw-line)
  * `Render/Export`: see [Render/Export](#renderexport)
  * `View Point Cloud`: see [View Point Cloud](#view-point-cloud)
  * a `?` button: this button will direct you to this repository and readme documentation.

A MacOS 11.0.1 display of the main menu should look like the menu below.
  
![Image of Main Menu](https://github.com/nchaconbgeo/pointcloudpackage/blob/52e50232f70f1181900d37183f385c8311e2cfbd/5LM8NSSPHYK7F1Tk6wDMWapX95uX_1i72NGmp0vEPue0i4H4XdKcnLZjElpvhE3AkI8uStRGPqCTLEp3Gy7mfDQL-4KT0yHWYlaUdmEhQENTtlAZXpWwi-kOLCGN4aY0ZYp8qnxBzYY.png)
  
#### Select Volume
Before clicking `Select volume`, you can assign or create a label for the volume selected as well as give the area selected a name, description, and color in the [`Edit/View Labels`](#editview-labels) menu. In the example below, "Sandstone" is selected as the rock type. 

![Example of Created Classifications](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/classifications_contact.png)

Upon clicking `Select Volume`, you will be directed to an [open3D VisualizerWithEditing()](http://www.open3d.org/docs/latest/python_api/open3d.visualization.VisualizerWithEditing.html) window and the main menu for the app will disappear. At this point you will be able to select the points to form your volume selection on the cloud, as shown in the image below. Note that the application will select your volume for labelling based on a bounding polygon you draw around the points you would like to select. 

![Points Selected on Cloud](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/VolSelectPoints.png)

Some pertinent commands for selecting your volume include:
 * `shift + left click`: Select a point in the point cloud to begin forming your polygon for volume selection. 
 * `shift + right click`: "Undo" your last point selection in your volume selection.
 * `q` key or `esc` key: Close the window when you are finished making your volume selection.

Note that you must choose at least four points to form a polygon that will select a volume effectively. To view your labeled point cloud after selecting a volume, use `View Point Cloud` from the main screen.

![Labelled Cloud](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/Volume.png)

#### Edit/View Labels
Upon clicking `Edit/View labels` for the first time in the application, an empty classification menu will pop up as shown below:

![New Classification Window](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/point_classification_contact.png)

To create a new classification, click the `New Classification` button and a prompt will appear with the fields "Name", "Classification", and "Color". If "Color" is clicked then a color picker menu will appear as well. These two windows are displayed below.

![New Classification Prompt](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/new_type_contact.png)
![Color Picker](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/color_picker_contact.png)

Once a new classification is added, it will appear in the list and can be selected as the current rock type to be classified by selecting its corresponding radio button to the left of the name. In the example below, two classifications were created, named "Sandstone" and "Mudstone", and the current selected classification for volume selection and labelling is "Sandstone".

![Example of Created Classifications](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/classifications_contact.png)


#### Draw Line
Upon clicking `Draw Line`, an [open3D VisualizerWithEditing()](http://www.open3d.org/docs/latest/python_api/open3d.visualization.VisualizerWithEditing.html) will appear and you will be able to select the points to form your lines.

Some pertinent commands for selecting your line's points include:
 * `shift + left click`: Select a point in the point cloud to begin forming your polygon for volume selection. 
 * `shift + right click`: "Undo" your last point selection in your volume selection.
 * `q` key or `esc` key: Close the window when you are finished making your volume selection.

An example of line select is shown below. The first image is the user selected points before pressing `q` to quit the visualizer and choose a color. The second image is from clicking `View Point Cloud` which now displays the the line set created by connecting the points in order of selection. Note that the +/- button changes the point size in display, which is why point sizes are different in the two examples.

![Line Selected](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/points_selection_line.png)
![Line drawn](https://github.com/nchaconbgeo/pointcloudpackage/blob/main/line_drawn_example.png)

#### Render/Export:
Upon clicking `Render/Export`, you will be prompted to select how you would like to render the files. 

The options for file export include:
  * Export a photo of the point cloud as a .png: You will be able to position the camera in open3D to get the angle you would like for the photo, and then press `q` or `esc` to close the open3D window and save the photo.
  * Export colored point cloud: the current point cloud will be exported as a .pcd with all color information retained from the user's interactions with the data. 
  * Export as separate point cloud: the recolored point cloud will be exported, and an individual point cloud will be exported for each class with all original point information. Note that this option creates several files. 

#### View Point Cloud:
Upon clicking `View Point Cloud`, an [open3D Visualizer()](http://www.open3d.org/docs/latest/python_api/open3d.visualization.Visualizer.html) window will display on your screen for displaying the points. To exit this window and go back to the main app, press `q` or `esc`.

## Installation
This application requires Python version >3.8 to run, with `pip` installed on the computer. The following command block will install all required dependencies for GeoPointClouds.

`pip install open3d numpy tk` 

Next, download this github repository into a folder of your choice. 

`cd ~/my/file/path/example`  
`git clone https://github.com/nchaconbgeo/pointcloudpackage`

### MacOS Quick Start and Windows Use
To launch the app from here, navigate to the src folder in point cloud package. Assuming you are located in the example directory above (`~/my/file/path/example`), you would use the commands:

`cd pointcloudpackage/src`  
`python3 application.py`

### MacOS Desktop Icon Creation

If you would like a Desktop App to run the app from, you can follow the instructions on this [website.](https://martechwithme.com/convert-python-script-app-windows-mac/)

A video tutorial that outlines the instructions from the website above with specific reference to GeoPointClouds is available here: [https://www.youtube.com/watch?v=v9F55mZe7hw](https://www.youtube.com/watch?v=v9F55mZe7hw)


## Open3D Use Help
[Open3D's documentation](http://www.open3d.org/docs) has some useful information for navigating the open3D window. A simple tutorial on Open3D visualization can be found [here](http://www.open3d.org/docs/latest/tutorial/Basic/visualization.html). For this project, all visualized windows are either open3D.visualization.Visualizer() objects and open3D.visualization.VisualizerWithEditing() objects. Hence, these are the types of visualizers that we recommend getting accustomed to and familiar with the documentation on.

## Message for Developers

Documentation for code can be found either within the code, or consolidated in a sphinx html format in _build/html/index.html
