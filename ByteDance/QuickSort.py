# -*- coding: utf-8 -*-
# @Time   : 2019/12/16 8:42 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: QuickSort.py
# @Software: PyCharm

# 快速排序
def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    arr = [5, 23, 24, 13, 54, 66, 1, 323, 56, 545]
    print(quicksort(arr))
