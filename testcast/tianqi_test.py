#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: tianqi_test.py
@time: 2021/1/4 15:57
@desc:
'''


import unittest
from ddt import ddt,file_data
import configparser

from api.api_keyd import ApiKd
from log.mylog import Log


@ddt
class TianQi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Log().info('TIANQI_API setup class')
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        cls.url = conf.get('TIANQI_API','url')
        cls.appid = conf.get('TIANQI_API','appid')
        cls.appsecret = conf.get('TIANQI_API','appsecret')
        cls.version = conf.get('TIANQI_API', 'version')
        cls.ak = ApiKd()



    @file_data('../data/tianqi_data.yaml')
    def test_1(self,**kwargs):
        Log().debug('ddt 数据传入 ,测试数据和代码分离 进行测试')
        req_city = kwargs['param']['city']

        ass_city = kwargs['text']

        url = self.url+"appid="+self.appid+"&appsecret="+self.appsecret+"&version="+self.version+"&city="+req_city
        print(url)
        Log().debug('执行测试')
        data = self.ak.get(url=url).text
        print(data)

        res_city = self.ak.get_text(data,'city')
        print(res_city)

        self.assertEqual(req_city,ass_city,msg='验证失败 !')



if __name__ == '__main__':
    unittest.main()
