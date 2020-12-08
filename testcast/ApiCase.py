#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: ApiCase.py
@time: 2020/12/7 13:50
@desc:
'''


from Api.Api_keyd import *

import unittest
from ddt import ddt,data,file_data,unpack
import configparser
import yaml
import jsonpath
import json


@ddt
class ApiDemo(unittest.TestCase):

    '''
    执行步骤 :
    1.读取配置文件
    2.读取case数据 ,拼接测试数据
    3.通过ddt数据驱动,执行测试用例, 包括里面接口的关联
    4.输出测试结果
    '''

    @classmethod
    def setUpClass(cls):
        cls.tmp = None
        # 读取配置文件
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')

        cls.url = conf['WEATHER']['url2']
        print(cls.url)

        cls.ak = ApiKd()


    @file_data(r'../data/weather_data.yml')
    @unpack
    def test_1_one(self,**kwargs):

        # 读取数据文件
        # ym_file = open('../data/weather_data.yml','r')
        # ym = yaml.load(ym_file,yaml.FullLoader)
        # print(ym['city'])
        # with open(r'../data/weather_data.yml','r') as f:
        #     tmp = yaml.load(f.read(),yaml.FullLoader)
        #     print(tmp['case1']['city'])
        #     print(tmp['case1']['text'])
        #     city = tmp['case1']['city']
        #     text = tmp['case1']['text']


        city =kwargs['param']['city']
        exc_text = kwargs['text']
        # 拼接数据
        self.url += str(city)+".html"
        print(self.url)

        # 测试请求
        res = self.ak.get(url=self.url).text


        text_json = json.loads(res,encoding='utf-8')
        print(text_json)

        print(json.dumps(text_json))
        print(type(json.dumps(res)))



        res_ret = jsonpath.jsonpath(text_json,'$..city')
        print(res_ret)


        ApiDemo.tmp = res_ret[0]


    def test_2_te(self):

        print(self.tmp)








if __name__ == '__main__':
    unittest.main()