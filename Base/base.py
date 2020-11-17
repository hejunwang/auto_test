#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: base.py
@time: 2020/11/17 13:18
@desc:
'''



class Base:
    '''
    init 初始化
    '''
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    '''
    打开
    '''
    def open(self):
        self.driver.get(self.url)

    '''
    元素获取
    '''
    def clamator_element(self,clamator_id):
         return self.driver.find_element(*clamator_id)

    '''
    关闭
    '''
    def quit(self):
        self.driver.quit()