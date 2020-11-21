#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: mytest.py
@time: 2020/11/12 21:32
@desc:
'''

import unittest
import requests
import jsonpath
import json

class MyTestSuit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupclass-----\n")
        pass

    @classmethod
    def tearDownClass(cls):
        print("teardownclass---")
        pass


    def test_case1(self):


        url = "http://35.215.171.22:5000/bookstore/api/v1/books"
        re = requests.get(url).text
        print(re)
        print(type(re))
        # 把json格式字符串转换成python对象
        resp = jsonpath.jsonpath(json.loads(re),'$.books[0].title')
        print(resp)

        assert '论语' ==resp[0],'判断失败'






if __name__ == '__main__':
    unittest.main()

