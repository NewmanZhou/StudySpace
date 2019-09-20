# --*- coding: utf-8 -*-
'''
Python: Singleton (单例模式)
主要完成两件事：
1、只允许Singleton 类生成一个实例。
2、如有已经有一个实例了，我们会重复提供同一个对象
'''
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance

s = Singleton()
print(s)
s1 = Singleton()
print(s1)

# 懒汉式实例化
class LazySingleton(object):
    __instance = None
    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created:")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance
s = LazySingleton()
print("Object created",LazySingleton.getInstance())

s1 = LazySingleton()
print(s1.getInstance())

