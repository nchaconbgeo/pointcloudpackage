import pytest
import open3d as o3d
import numpy as np
import os, sys
from .. import import_export

class TestImport:
    def setUp(self):
        format = "x y z r g b alpha nx ny nz"
        # print("initiating file processesing")
        inputFormat = import_export.txtToPcd("sample_data/Mudstone.txt", "sample_data/Mudstone_parsed.txt", format)
        # print("finished importing file")
        print(inputFormat)
        self.pcd = o3d.io.read_point_cloud("sample_data/Mudstone_parsed.txt", inputFormat)
        self.original_colors = []
        self.original_colors = self.pcd.colors
        self.classes = np.zeros(len(self.pcd.points))   


    def test_InputTypeAndLength(self):
            self.setUp()
            assert(isinstance(self.pcd, o3d.geometry.PointCloud))
            assert(len(self.pcd.points) == len(self.original_colors))
            assert(len(self.classes) == len(self.original_colors))
            assert(len(self.pcd.points) == 2086781) #number of non-blank lines in Mudstone.txt
        
