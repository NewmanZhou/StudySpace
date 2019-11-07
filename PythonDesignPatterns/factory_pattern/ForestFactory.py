# -*- coding: utf-8 -*-
# @Time   : 2019/11/4 9:51 AM
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: ForestFactory.py
# @Software: PyCharm

'''
简单工厂模式： 允许接口创建对象，但不会暴露对象的
工厂方法模式： 允许接口创建对象，但使用哪个类来创建对象，则是交由子类决定的。
抽象工厂模式： 抽象工厂是一个能够创建一系列相关的对象而无需指定/公开其具体类的接口。
该模式能够提供其他工厂的对象，在其内部创建其他对象。
'''  #

from abc import ABCMeta, abstractclassmethod


class Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


# forest factory defind
class ForsetFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForsetFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
    # Animal().do_say()
