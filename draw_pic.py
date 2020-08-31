# 本程序从Excel表格读入数据并绘制三维散点图

# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
# import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

data_frame_1 = pd.read_excel('LCOE_data_1.xlsx',sheet_name='Sheet1')
# print (data_frame[])
x_1 = data_frame_1['Net Capacity Factor']
y_1 = data_frame_1['Generation Equipment']
z_1 = data_frame_1['LCOE']
ax_1 = plt.subplot(111, projection='3d')
ax_1.scatter(x_1, y_1, z_1, c='y')

ax_1.set_xlabel('Net Capacity Factor')
ax_1.set_ylabel('Generation Equipment')
ax_1.set_zlabel('LCOE')

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.savefig('lcoe_pic_1.jpg')


data_frame_2 = pd.read_excel('LCOE_data_2.xlsx',sheet_name='Sheet1')
# print (data_frame[])
x_2 = data_frame_2['Generation Equipment']
y_2 = data_frame_2['Percentage']
z_2 = data_frame_2['LCOE']
ax_2 = plt.subplot(111, projection='3d')
ax_2.scatter(x_2, y_2, z_2, c='r')

ax_2.set_xlabel('Generation Equipment')
ax_2.set_ylabel('Percentage')
ax_2.set_zlabel('LCOE')

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.savefig('lcoe_pic_2.jpg')

data_frame_3 = pd.read_excel('LCOE_data.xls',sheet_name='organized_data')
# print (data_frame[])
x_3 = data_frame_3['发电能力']
y_3 = data_frame_3['总投资']
z_3 = data_frame_3['LCOE']
ax_3 = plt.subplot(111, projection='3d')
ax_3.scatter(x_3, y_3, z_3, c='r')

ax_3.set_xlabel('Generating capacity')
ax_3.set_ylabel('Total investment')
ax_3.set_zlabel('LCOE')

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.savefig('lcoe_pic_3.jpg')