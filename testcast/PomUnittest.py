#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: PomUnittest.py
@time: 2020/11/17 16:04
@desc:
'''

import unittest
from selenium import webdriver
from Page.page import *
from ddt import ddt,data,unpack

@ddt
class pomunittest(unittest.TestCase):

    def setUp(self):
        pass
        self.driver = webdriver.Chrome()


    def tearDown(self):
        pass
        self.driver.implicitly_wait(5)
        self.driver.quit()

    @data(('http://www.baidu.com','python'),('http://www.baidu.com','python3'))
    @unpack
    def test_one(self,url,text):
        sp = SearchPage(self.driver, url)
        sp.open()
        sp.input_text(text)
        sp.click()



if __name__ == '__main__':
    unittest.main()