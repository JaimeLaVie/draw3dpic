# 本程序从“LCOE制表数据”读入数据并转成draw_pic.py需要的格式，保存为LCOE_data.xls

# -*- coding: utf-8 -*-
import pandas as pd
import xlwt
import numpy as np

data_frame = pd.read_excel('LCOE制表数据.xlsx',sheet_name='Sheet1')
data_frame = data_frame.values
print (data_frame)
print (np.shape(data_frame))
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('organized_data')
posit_1 = 0
posit_2 = 0
posit_4 = 1
posit_6 = 2
for i in range(11):
    x = 0.15 + 0.002 * i
    for j in range(41):
        y = 0.6 + 0.01 * j
        worksheet.write(posit_1, posit_2, x)
        worksheet.write(posit_1, posit_4, y)
        worksheet.write(posit_1, posit_6, data_frame[j, i])
        posit_1 += 1
workbook.save('LCOE_data.xls')
