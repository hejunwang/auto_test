#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: ci_jenkins_py.py
@time: 2020/12/16 17:27
@desc:
'''

import jenkins

# server = jenkins.Jenkins('http://localhost:8080', username='admin', password='123456')
# user = server.get_whoami()
# version = server.get_version()
# print('Hello %s from Jenkins %s' % (user['fullName'], version))
#
# dict = {'key1':1,'key2':2}
# for key ,value in dict.items():
#     print(key)
#     print(value)
#
# print(dict.keys())
# print(len(dict))




# 闭包函数定义 :内部函数引用了外部函数中的变量,以下是闭包函数的两种形式
# 作用 :保存函数的状态信息 ,使函数的局部变量信息可以保存下来

def fun1():
    num = 8
    def fun2():
        print(num)
    print(fun2.__closure__)        # 判断是否是一个闭包函数 ,是闭包返回一个cell ,否则返回为None
    return fun2


def fun1_1(x):
    def fun2():
        print(x)
    print(fun2.__closure__)        # 判断是否是一个闭包函数 ,是闭包返回一个cell ,否则返回为None
    return fun2





#装饰器   : 装饰器其实就是一个闭包,把一个函数作为参数 ,然后返回一个替代版函数 ,
def outter_fun(fun):
    def inner():
        print(" xxxx")
        ret = fun()+1
        print(ret)
        return ret
    print(inner.__closure__)
    return  inner




def outter_fun2(func):
    def wrapper(*args,**kwargs):
        print("outter_fun2 装饰器")
        return func(*args,**kwargs)

    return wrapper


@outter_fun2
def inner_fun(x,y):
    print('@装饰器')
    return x+y

def _fun():
    print('_fun')
    return 2


def hex_to_dec(value):
    return int(value,16)


if __name__ == '__main__':
    # ff = fun1_1(2)
    # ff()

    of = outter_fun(_fun)
    of()

    b = hex_to_dec("0xB")

    print(b)

    a= int("0xA",16)
    print(a)

