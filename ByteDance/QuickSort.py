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


def QuickSort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return QuickSort(less) + [pivot] + QuickSort(greater)


# 选择排序
def findSmallest(arr):
    smallest = arr[0]  # 存储最小的值
    smallest_index = 0  # 存储最小值的索引
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr


if __name__ == '__main__':
    arr = [5, 23, 24, 13, 54, 66, 1, 323, 56, 545]
    print(QuickSort(arr))
