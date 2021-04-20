# -*- coding: utf-8 -*-
# @Time   : 2020/12/23 4:14 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: DisposeExcel.py
# @Software: PyCharm
from Utils import Utils
import openpyxl

# 文件的绝对路径 ， 文件名称
xlsfilepath = "/Users/newmanzhou/PythonSpace/Code/myTestSpace/gitSpace/StudySpace/for_baby"
fileName = "forbaby.xlsx"


def findExcelFile():
    dataList = myUtils.ReadExcelToList(xlsfilepath + '/' + fileName)
    disposeDataList(fileName, dataList)


def disposeDataList(fileName, dataList):
    ItemType = ['中间件组', '数据库组', '微服务组', '容器平台组']
    # 用于接收每组的各项工作时间
    ZJJZDict = {}
    SJKZDict = {}
    WFWZDict = {}
    RQPTZDict = {}
    # 用于记录每组的总时间
    ZJJZTime = 0
    SJKZTime = 0
    WFWZTime = 0
    RQPTZTime = 0

    for data in dataList:
        classType = data[0]
        if classType == ItemType[0]:
            ZJJZTime += data[2]
            ZJJZDict[data[1]] = (ZJJZDict.get(data[1], 0) + data[2])
        elif classType == ItemType[1]:
            SJKZTime += data[2]
            SJKZDict[data[1]] = (SJKZDict.get(data[1], 0) + data[2])
        elif classType == ItemType[2]:
            WFWZTime += data[2]
            WFWZDict[data[1]] = (WFWZDict.get(data[1], 0) + data[2])
        elif classType == ItemType[3]:
            RQPTZTime += data[2]
            RQPTZDict[data[1]] = (RQPTZDict.get(data[1], 0) + data[2])

    wb = openpyxl.load_workbook(r'forbaby.xlsx')
    ws = wb.create_sheet(title='分析结果')
    ws.append(["所属职能组", "工作类型", "总工时", "百分比", "各组总工时"])

    # 中间件组 数据写入新表
    for key, value in enumerate(ZJJZDict.items()):
        percentage = '{:.2%}'.format(value[1] / ZJJZTime)
        if key == 0:
            ws.append([ItemType[0], value[0], value[1], percentage, ZJJZTime])
        else:
            ws.append([ItemType[0], value[0], value[1], percentage])

    # 数据库组 数据写入新表
    for key, value in enumerate(SJKZDict.items()):
        percentage = '{:.2%}'.format(value[1] / SJKZTime)
        if key == 0:
            ws.append([ItemType[1], value[0], value[1], percentage, SJKZTime])
        else:
            ws.append([ItemType[1], value[0], value[1], percentage])

    # 微服务组 数据写入新表
    for key, value in enumerate(WFWZDict.items()):
        percentage = '{:.2%}'.format(value[1] / WFWZTime)
        if key == 0:
            ws.append([ItemType[2], value[0], value[1], percentage, WFWZTime])
        else:
            ws.append([ItemType[2], value[0], value[1], percentage])

    # 容器平台组 数据写入新表
    for key, value in enumerate(RQPTZDict.items()):
        percentage = '{:.2%}'.format(value[1] / RQPTZTime)
        if key == 0:
            ws.append([ItemType[3], value[0], value[1], percentage, RQPTZTime])
        else:
            ws.append([ItemType[3], value[0], value[1], percentage])

    wb.save(fileName)
    print("数据处理完成")

if __name__ == '__main__':
    myUtils = Utils()
    findExcelFile()
