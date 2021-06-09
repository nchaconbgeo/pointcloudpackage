## GeoPointClouds 3D Visualization Software

GeoPointClouds is a 3D Visualization Software created to perform geological interpretations on point cloud data. Version 0.0 functionality consists of:
  * File Input and Output for Point Cloud Data Types:
    *   .txt<sup> 1</sup>
    *   .ply 
    *   .pcd
    *   .pts
  * Graphical Visualization of 3d Point Clouds:
    * Color Changes for Data
    * Ability to rotate and perform zoom operations on data  
  * Volume Selection for Point Cloud Labeling
    * Polygon Selection
    * Projection Selection
  * Line drawing functionality
  * Graphical User Interface

All functionality is contained within an application that can be run as an executable on MacOS and Windows. 

<sup>1</sup> User must specify format in Import File for .txt. 

## Basic App Navigation

Upon launching the application, you will be see an import file menu to load your file in for use. The components of this menu consist of:
  * a `select file` button: this will launch your file explorer to locate the point cloud file. 
  * a `file format` entry box: if you are using a .txt file, this is where you will define the file heading format, such as 'x y z r b g' or 'x y z r g b nx ny nz'
  * a `done` button: click to begin processing your point cloud file for the program. 
![Image of File Import Menu](https://github.com/nchaconbgeo/pointcloudpackage/blob/880882d4609b8b2aa132f7eb7d34bdbd2db4bf9d/R3dF8LChjjVPzA0pDqUXoSYy9t1eK2RRW5jquabGel_H5_XPiKdv2jDJfidlsbG88s8_LCcRUvSiqM7aY-i3iiDwUG50hAhSVn_FPrI4dMeyWPMZ6fCetf_L04XTLexrpRpJEQNS_vo(1).png)

## Developer Documentation

*Message for Developers:* Documentation for code can be found either within the code, or in a sphinx format in _build/html/index.html
