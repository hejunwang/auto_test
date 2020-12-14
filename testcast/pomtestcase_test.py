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
import os,time




@ddt
class PomUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 这里使用了无头配置的option
        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        cls.driver = webdriver.Chrome(options=option)
        # 登录页面page
        cls.lp = LoginPage(cls.driver)
        # 首页page
        cls.ip = IndexPage(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # def tearDown(self):
    #     # 这里查看了源码里中_outcome =_Outcome () 这个类 ,_Outcome类中有success ,errors 这样的结果保存
    #     if len(self._outcome.errors)>=1:
    #         print('测试CASE中有失败的情况,执行下面的截图 self._outcome.errors ' %self._outcome.errors)
    #         currentPath = os.getcwd()  # 当前目录
    #         parent_path = os.path.dirname(currentPath)  # 将当前目录传入得到当前目录的父目录
    #         img_path = os.path.join(parent_path, 'img')
    #
    #         current_time = time.strftime('%Y-%m-%d-%H%I%M%S', time.localtime(time.time()))
    #         file_name = os.path.join(img_path, current_time + ".png")
    #         print('filename-->{}'.format(file_name))
    #
    #         self.screen_file(file_name)
    #
    #
    # def screen_file(self,filename):
    #     self.driver.get_screenshot_as_file(filename=filename)

    def test_1(self):
        print('测试的异常,异常后 ,再退出的时间 ,会执行teardown ,然后再进行截图 ')
        self.assertEqual(1, 2, '我是个异常验证')



    @file_data('../data/userinfo.yaml')
    def test_3_(self,**kwargs):
        print('这个case中引入了 无头页面显示')
        # 业务流程: 登录--> 应用切换-->发送邮件 -->接受邮件
        # 输入账户密码 # 登录确认
        self.lp.login(kwargs['user'], kwargs['passwd'])
        self.lp.wait_(kwargs['time_'])

        # 登录后,应用切换
        self.ip.index_all()
        self.ip.wait_(kwargs['time_'])

        print('无头页面模式也是可以正常的进行测试,我增加一点测试的异常看下')
        self.assertEqual(1, 1, '我是个异常验证')







if __name__ == '__main__':
    unittest.main()

