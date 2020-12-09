#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: Api_keyd.py
@time: 2020/12/7 13:47
@desc:
'''


import jsonpath
import requests

class ApiKd:
    '''
    关键字定义两个方法 get post方法
    '''
    def get(self,url,headers=None,params=None):

        return requests.get(url,headers=headers,params=params)


    def post(self,url,headers=None,data=None):

        return  requests.post(url,headers=headers ,data = data)


    def put(self):

        pass


    def update(self):
        pass




    # 从json文件中获取到指定key的 value,返回的是list ,取第一个值
    def get_text(self,res,text):

        if res is not None:
            value = jsonpath.jsonpath(res,'$..{0}'.format(text))
        else:
            return None
        return value[0]


