# -*- coding: utf-8 -*-

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
print 'Before sort: '
for p in List:
    print p.toString()
# 根据年龄 进行正序排列
List.sort(lambda p1, p2: cmp(p1.age, p2.age))
print '/n After ascending sort：'
for p in List:
    print p.toString()
# 根据年龄 倒叙排列
List.sort(lambda p1, p2: -cmp(p1.age, p2.age))
print '/n After descending sort'
for p in List:
    print p.toString()
