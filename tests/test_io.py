import pytest
import open3d as o3d
import numpy as np
import os, sys


class TestImport:
    def setUp(self):
            format = "x y z r g b alpha nx ny nz"
            # print("initiating file processesing")
            # txt_to_pcd("C:/Users/specs/Open3D_PC/Mudstone.txt", "C:/Users/specs/Open3D_PC/Mudstone1.pcd", format)
            # print("finished importing file")
            self.pcd = o3d.io.read_point_cloud("../sample_data/face.ply")
            self.original_colors = []
            self.original_colors = self.pcd.colors
            self.classes = np.zeros(len(self.pcd.points))   

    def test_InputTypeAndLength(self):
            self.setUp()
            assert(isinstance(self.pcd, o3d.geometry.PointCloud))
            assert(len(self.pcd.points) == len(self.original_colors))
            assert(len(self.classes) == len(self.original_colors))
        
