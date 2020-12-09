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


    # 解析读取文件中的字典

    def assigndict(self,kwargs):

        for key ,value in kwargs.items():

            if type(value) is dict:
                print(value)
                return self.assigndict(value)

            else:
                if value:
                    print(value)
                    kwargs[key] = getattr(self,key)
                    print(kwargs[key])
                else:

                    kwargs[key] = getattr(kwargs,key)

        return kwargs


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

        # 获取参数cityid,参数对应城市
        cityId =kwargs['param']['city']
        print('request cityid: %s' %cityId)

        cityText = kwargs['text']

        # 拼接数据
        self.url += str(cityId)+".html"
        print(self.url)

        # 测试请求
        res = self.ak.get(url=self.url).text
        text_json = json.loads(res,encoding='utf-8')
        print(text_json)

        res_ret =self.ak.get_text(text_json,'cityid')
        print('response cityid : %s' %res_ret)

        # 请求结果校验
        self.assertEqual(str(cityId),res_ret,'cityid参数和结果对比失败')

        # 这里可以设置公共的变量 作为全局的变量 ,其他接口的依赖
        ApiDemo.tmp = res_ret[0]



    def test_3(self):
        # 使用到前面返回的结果 ,作为参数进行传递
        print(self.tmp)


if __name__ == '__main__':
    unittest.main()