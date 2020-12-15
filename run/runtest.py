#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: runtest.py
@time: 2020/12/11 14:34
@desc:
'''



# 添加测试用例
# 执行测试用例
# 输出测试报告
# 发送中测试报告

import unittest

from BeautifulReport import BeautifulReport
from emailsend.send_email import sendEmail
import time,os,sys

sys.path.append('../')


currentPath = os.getcwd()  # 当前目录
parent_path = os.path.dirname(currentPath)  #将当前目录传入得到当前目录的父目录

def runstart():
    # 配置case地址和报告地址
    case_dir = os.path.join(parent_path,'testcast')
    report_path= os.path.join(parent_path,'Report')
    print(report_path)

    # 搜索case
    suite_tests = unittest.defaultTestLoader.discover(case_dir, pattern="*_test.py",
                                                      top_level_dir=None)
    # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例

    current_time =time.strftime('%Y-%m-%d-%H%I%M',time.localtime(time.time()))
    file_name = current_time+".html"

    # 测试报告输出,report_dir=' 指定目录下
    BeautifulReport(suite_tests).report(filename=file_name, description='关键字数据驱动测试',
                                        report_dir=report_path)



    # 发送邮件
    sendEmail().send_email()



if __name__ == '__main__':
    runstart()