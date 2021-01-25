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

from BeautifulReport import BeautifulReport

from log.mylog import Log

currentPath = os.getcwd()  # 当前目录


parent_path = os.path.dirname(currentPath)  # 将当前目录传入得到当前目录的父目录
# img_path = os.path.join(parent_path, 'image')
img_path = os.path.abspath(os.path.dirname(os.getcwd()))+"\image"

# current_time = time.strftime('%Y-%m-%d-%H%I%M%S', time.localtime(time.time()))
# file_name = os.path.join(img_path, current_time + ".png")
# print('filename-->{}'.format(file_name))
print('img_path-->{}'.format(img_path))


@ddt
class PomUnit(unittest.TestCase):
    # 定义一个保存截图函数
    def save_img(self,img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))


    @classmethod
    def setUpClass(cls):
        Log().info(' PomUnit  setUpClass')
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
        Log().info('tearDownClass')
        cls.driver.quit()


    # def tearDown(self):
    #     # 这里查看了源码里中_outcome =_Outcome () 这个类 ,_Outcome类中有success ,errors 这样的结果保存
    #     if len(self._outcome.errors)>=1:
    #         print('测试CASE中有失败的情况,执行下面的截图 self._outcome.errors ' %self._outcome.errors)
    #
    #
    #
    # def screen_file(self,filename):
    #     self.driver.get_screenshot_as_file(filename=filename)


    # @BeautifulReport.add_test_img('test_errors_save_imgs')
    def test_1(self):
        # try:
        Log().info('PomUnit  testing 中的测试日志打印 ')
        self.assertEqual(1, 3, '我是个异常验证')
        # except Exception as e:
        #     print('异常原因 :%s' % e)
        #     currentPath = os.getcwd()  # 当前目录
        #     parent_path = os.path.dirname(currentPath)  # 将当前目录传入得到当前目录的父目录
        #     img_path = os.path.join(parent_path, 'image')
        #
        #     current_time = time.strftime('%Y-%m-%d-%H%I%M%S', time.localtime(time.time()))
        #     file_name = os.path.join(img_path, current_time + ".png")
        #     print('filename-->{}'.format(file_name))
        #     # 图片名称可以加个时间戳
        #     # nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        #     # self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
        #     self.driver.get_screenshot_as_file(filename=file_name)
        #     raise


    # @BeautifulReport.add_test_img('test_3.png')
    @file_data('../data/userinfo.yaml')
    def test_3_(self,**kwargs):
        print('这个case中引入了 无头页面显示')
        # 业务流程: 登录--> 应用切换-->发送邮件 -->接受邮件
        # 输入账户密码 # 登录确认
        try:
            self.lp.login(kwargs['user'], kwargs['passwd'])
            self.lp.wait_(kwargs['time_'])
            Log().info('testing 中的测试日志打印 ')
            # 登录后,应用切换
            self.ip.index_all()
            self.ip.wait_(kwargs['time_'])

            Log().info('无头页面模式也是可以正常的进行测试,我增加一点测试的异常看下')
            self.assertEqual(1, 2, '我是个异常验证')
        except Exception as e:
            print('异常原因 :%s' %e)
            Log().info('testing 异常情况下,调用save_img函数 ')
            # self.save_image(img_path,'test_3.png')
            raise



if __name__ == '__main__':
    unittest.main()

