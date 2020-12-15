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
from Page.searchpage import *
from ddt import ddt,data,unpack,file_data

from configparser import ConfigParser

import time,os




@ddt
class pomunittest(unittest.TestCase):

    def setUp(self):
        pass
        self.driver = webdriver.Chrome()


        # 读取配置文件
        config = ConfigParser()
        config.read('../config/config.ini')
        self.addr = config.get('DEFAULT','url')
        print(self.addr)


    def tearDown(self):

        self.driver.implicitly_wait(5)

        # 这里查看了源码里中_outcome =_Outcome () 这个类 ,_Outcome类中有success ,errors 这样的结果保存
        if len(self._outcome.errors) >= 1:
            print('测试CASE中有失败的情况,执行下面的截图 self._outcome.errors :%s ' % len(self._outcome.errors))

            for i in self._outcome.errors:
                print(i)
            currentPath = os.getcwd()  # 当前目录
            parent_path = os.path.dirname(currentPath)  # 将当前目录传入得到当前目录的父目录
            img_path = os.path.join(parent_path, 'img')

            current_time = time.strftime('%Y-%m-%d-%H%I%M%S', time.localtime(time.time()))
            file_name = os.path.join(img_path, current_time + ".png")
            print('filename-->{}'.format(file_name))

            self.screen_file(file_name)
        self.driver.quit()



    def screen_file(self,filename):
        self.driver.get_screenshot_as_file(filename=filename)

    # ddt驱动数据
    @file_data('../data/search.yaml')
    @unpack
    def test_3(self,**kwargs):
        sp = SearchPage(self.driver)
        sp.search(kwargs['palyload']['url'],kwargs['text'])


  # ddt驱动数据
    @data(('http://www.baidu.com','python'),('http://www.baidu.co','python3'))
    @unpack
    def test_4(self,url,text):
        sp = SearchPage(self.driver)
        sp.search(url,text)

    # ddt驱动数据
    @data(('http://www.baidu.com', 'python'), ('http://www.baidu.co', 'python3'))
    @unpack
    def test_4(self, url, text):
        sp = SearchPage(self.driver)
        sp.search(url, text)





if __name__ == '__main__':
    unittest.main()
