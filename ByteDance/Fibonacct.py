# -*- coding: utf-8 -*-
# @Time   : 2020/12/25 4:05 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: Fibonacct.py
# @Software: PyCharm
'''
使用生成器实现 斐波那契数列
'''
from collections.abc import Iterable,Iterator


class Fibonacct(object):
    def __init__(self, nums):
        self.__nums = nums
        self.__current_num = 0
        self.__a = 0
        self.__b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_num < self.__nums:
            ret = self.__a
            self.__a, self.__b = self.__b, self.__a + self.__b
            self.__current_num += 1
            return ret

        else:
            raise StopIteration


if __name__ == '__main__':
    fb = Fibonacct(10)
    print(isinstance(fb,Iterator))
    listData = [a for a in Fibonacct(20)]
    print(listData)
