# -*- coding: utf-8 -*-
# @Time   : 2020/2/3 2:47 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: Solution.py
# @Software: PyCharm

class Solution(object):
    # 数据找出两个数之和等于指定值的角标
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i




solution = Solution()
list = [0, 3, 5, 6, 7]
target = 8
data = solution.twoSum(list, target)
print(data)
