# -*- coding: utf-8 -*-
# @Time   : 2019/9/7 下午5:10
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : DisposeExcel
# @FileName: Utils.py
# @Software: PyCharm

import xlrd, xlwt
import os


# 处理本次需求的工具类， 主要以处理Excel为主
class Utils(object):

    def __init__(self):
        pass

    # 读取Excel 首张表格中的数据为list【】形式
    def ReadExcelToList(self, filepath):
        data = xlrd.open_workbook(filepath)
        table = data.sheets()[0]  # 通过索引顺序获取
        # table = data.sheet_by_index(0)  # 通过索引顺序获取
        # table = data.sheet_by_name(u'Sheet1')  # 通过名称获取

        # 获取行数和列数
        nrows = table.nrows
        ncols = table.ncols

        myDataList = []
        for i in range(nrows):
            line = []
            if i > 0:
                item = table.row_values(i)
                line.append(item[7])
                line.append(item[10])
                line.append(int(item[23]))
                myDataList.append(line)

        return myDataList

    # 文件删除
    def deleteExcel(self, filename):
        # 原有文件删除。
        os.remove(filename)

    # 文件移动
    # def moveExcel(self, startPath):
    #     movePath = settings.HistoryFolderPate
    #     shutil.move(startPath, movePath)

    # 精简表设置高亮
    def setColor(self, color, bold):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.colour_index = color
        font.bold = bold
        style.font = font
        return style
