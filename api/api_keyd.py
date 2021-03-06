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


import jsonpath,json
import requests
from time import sleep

class ApiKd:
    '''
    关键字定义两个方法 get post方法
    '''
    def get(self,url,headers=None,params=None):

        return requests.get(url,headers=headers,params=params)


    def post(self,url,headers=None,data=None):

        return  requests.post(url,headers=headers ,data = data)



    def get_text(self,res_string,key):
        '''
        从res是text
        从中 提取key   value 对应的值
        :param res:
        :param text:
        :return:
        '''
        if res_string is not None:
            res = json.loads(res_string)
            value = jsonpath.jsonpath(res,'$..{0}'.format(key))
        else:
            return None
        return value[0]


    def wait(self,time_):
        '''
        强制等待时间
        :param time_:
        :return:
        '''
        sleep(time_)



