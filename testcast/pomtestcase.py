#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: pomtestcase.py
@time: 2020/12/10 17:41
@desc:
'''



import unittest
from Page.loginpage import LoginPage
from Page.indexpage import IndexPage

from selenium import webdriver
from ddt import ddt,file_data



@ddt
class PomUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @file_data('../data/userinfo.yaml')
    def test_1_(self,**kwargs):
        # 输入账户密码 # 登录确认
        self.lp.login(kwargs['user'], kwargs['passwd'])
        # 登录后,应用切换
        self.ip.index_all()




if __name__ == '__main__':
    unittest.main()

