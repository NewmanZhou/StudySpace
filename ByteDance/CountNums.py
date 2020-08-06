# -*- coding: utf-8 -*-
# @Time   : 2020/7/13 4:18 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: CountNums.py
# @Software: PyCharm

# 给定一个无需数组，查询一个指定区间内，含有几个指定的数值。 这个查询要高效、快速、多次查询。
'''
实现方案， 将数组 转为 字典， 将值作为 key , 在数组中的位置角标作为  [value]  存成角标数组
再查询时，取对应的key 取出数组，对区间的起始位置、结束位置 做二分查找，查找比 （a, b ,8） a小的有几个
比 b + 1  小的有几个，  b-a 就是最终结果。
'''

class ListCountNums:
    def __init__(self, listArr):
        self.dictArr = self.listToDict(listArr)

    def listCountNus(self, tupeData):
        left = tupeData[0]
        right = tupeData[1]
        flag = tupeData[2]
        if self.dictArr[flag] is None:
            return 0
        else:
            listData = self.dictArr[flag]
            a = self.getArrCount(listData, left)
            b = self.getArrCount(listData, right + 1)
            return b - a

    def listToDict(self, listArr):
        dictArr = dict()
        for k in range(len(listArr)):
            if dictArr.get(listArr[k]) is None:
                dictArr[listArr[k]] = []
            dictArr.get(listArr[k]).append(k)

        return dictArr

    def getArrCount(self, listArr, num):
        left = 0
        right = len(listArr) - 1
        count = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if listArr[mid] < num:
                count = mid
                left = mid + 1
            else:
                right = mid - 1
        return count + 1


if __name__ == '__main__':
    listArr = [2, 2, 3, 4, 3, 2, 5, 3, 6, 7, 2, 6, 1, 7, 2]
    tupeData = (0,15,2)
    clazz = ListCountNums(listArr)
    print(clazz.listCountNus(tupeData))