# ==================================================
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : KimHuang
# @Organization : SDUST
# @E-mail: kim.huang.j@qq.com
# @Site : 
# @Time : 2021/5/12 10:32
# @File : test.py
# @Software: PyCharm
# @Desc : 
# ==================================================
import open3d as o3d
import numpy as np

print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("../test_data/fragment.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd], zoom=0.3412, front=[0.4257, -0.2125, -0.8795], lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
