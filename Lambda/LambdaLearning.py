# -*- coding: utf-8 -*-
import operator
from functools import reduce

# 根据 对象年龄 使用 Lambda 表达式进行排序
class People:
    age = 0
    gender = 'male'

    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def toString(self):
        return 'Age: ' + str(self.age) + ' Gender: ' + self.gender


List = [People(21, 'male'), People(20, 'famale'), People(34, 'name'), People(19, 'hello')]
print('Before sort: ')
for p in List:
    print(p.toString())
# 根据年龄 进行正序排列
List.sort(lambda p1, p2: operator.eq(p1.age, p2.age))
print('/n After ascending sort：')
for p in List:
    print(p.toString())
# 根据年龄 倒叙排列
List.sort(lambda p1, p2: - operator.eq(p1.age, p2.age))
print('/n After descending sort')
for p in List:
    print(p.toString())

# Lambda 基本使用
func = lambda x: x + 1
print(func(1))


# 等同于：
def func(x):
    return (x + 1)


foo = [1, 2, 4, 5, 7, 8, 9, 18]
print(list(filter(lambda x: x % 3 == 0, foo)))
print([x for x in foo if x % 3 == 0])

print(list(map(lambda x: x * 2 + 10, foo)))
print([x * 2 + 10 for x in foo])

print(reduce(lambda x, y: x + y, foo))
