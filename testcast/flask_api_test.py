#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: flask_api_test.py
@time: 2020/12/17 16:25
@desc:
'''


import unittest
from ddt import ddt,file_data,unpack
from api.api_keyd import ApiKd
from configparser import ConfigParser

import json



@ddt()
class FlaskApiUnit(unittest.TestCase):
    '''
    使用flask 作为服务端 ,登录的方式 ,user ,passwd
    接口测试
    '''
    @classmethod
    def setUpClass(cls):
        # config文件中读取url地址
        urlconf = ConfigParser()
        urlconf.read(r'../config/config.ini')
        cls.url = urlconf.get('FLASK_API','url')
        cls.ak = ApiKd()
        cls.headers = {'user-agent':
                       'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}


    @file_data('../data/login_flask.yaml')
    def test_1(self,**kwargs):

        # 地址的拼接 u
        name = kwargs['param']['name']
        pwd = kwargs['param']['pwd']

        assertcode  =kwargs['code']
        print(name)
        print(pwd)
        print(assertcode)
        print(self.headers)

        self.url = self.url+'name='+str(name)+'&pwd='+str(pwd)
        print('拼接后的地址 :'+self.url)

        # '地址请求'
        res = self.ak.get(self.url,self.headers).text
        self.ak.wait(2)
        # '解析返回的code'
        code =self.ak.get_text(res,'code')
        message =self.ak.get_text(res,'message')

        print(code)
        print(message)

        # 校验
        self.assertEqual(code,assertcode)






if __name__ == '__main__':
    unittest.main()


