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
from Page.page import *
from ddt import ddt,data,unpack
import yaml
from configparser import ConfigParser

import time,os
from BeautifulReport import BeautifulReport



@ddt
class pomunittest(unittest.TestCase):

    '''
    保存截图,这个功能暂时有问题
    '''
    def save_img(self, test_method):
        # 失败截图方法（必须要定义在class中）
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        print('root_dir-->{}'.format(root_dir))
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, test_method))


    def setUp(self):
        pass
        self.driver = webdriver.Chrome()
        # self.driver.get_screenshot_as_file()

        # 读取配置文件
        config = ConfigParser()
        config.read('../config/config.ini')
        self.addr = config.get('DEFAULT','url')
        print(self.addr)

        
        # 读取数据文件 yaml文件
        self.ym = open('../data/yamldata.yml','r')
        da = yaml.load(self.ym,yaml.FullLoader)

        print(da['text'])
        self.text = da['text']


    def test_case0(self):
        try:
            pass
            self.assertEqual('http://www.baidu.com1',self.addr,msg='和预期的结果不符合')

        except Exception as e:
            pass
            print('断言失败:{}'.format(e))
            raise e

    def test_case1(self):
        try:
            pass
            self.assertEqual('python3',self.text,msg='断言失败,验证失败')
        except Exception as e:
            print('异常:{}'.format(e))
            raise e



    def test_case2(self):
        sp = SearchPage(self.driver, self.addr)
        sp.open()


        sp.input_text(self.text)
        sp.click()



    def tearDown(self):
        pass
        self.ym.close()

        self.driver.implicitly_wait(5)
        self.driver.quit()


    # ddt驱动数据
    @data(('http://www.baidu.com','python'),('http://www.baidu.co','python3'))
    @unpack
    def test_one(self,url,text):
        sp = SearchPage(self.driver, url)
        sp.open()
        sp.input_text(text)
        sp.click()




if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(unittest.makeSuite(pomunittest))

    print('main unittest')

    now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
    localpath = os.getcwd()
    print('本文件目录位置：' + localpath)
    filepath = os.path.abspath(os.path.dirname(localpath) + os.path.sep + ".")+'\Report'

    print('报告存放路径' + filepath)

    filename = now +'.html'
    # 加载执行用例生成报告
    result = BeautifulReport(suite)
    # 定义报告属性
    result.report(description='Beautiful Report--自动化测试报告', filename=filename, report_dir=filepath)
