#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: indexpage.py
@time: 2020/12/10 15:26
@desc:
'''


from Base.basePage import BasePage

from selenium.webdriver.common.by import By

from selenium import webdriver

class IndexPage(BasePage):
    tongxunlu = (By.XPATH, '//*[@id="_mail_tabitem_1_117text"]')
    appcenter = (By.XPATH, '//*[@id="_mail_tabitem_2_118text"]')


    # 点击通讯录
    def app_send(self):
#         打开网页app 通讯录
        self.click_(self.tongxunlu)

#     app center
    def center(self):
        self.wait_(2)
        self.click_(self.appcenter)


    # 集成所有
    def index_all(self):
        self.app_send()
        self.wait_(2)
        self.center()


    # def assert_result(self,first,second):
    #     res = False
    #     if first ==second:
    #         res = True
    #         return res
    #     else:
    #
    #         import os,time
    #         currentPath = os.getcwd()  # 当前目录
    #         parent_path = os.path.dirname(currentPath)  # 将当前目录传入得到当前目录的父目录
    #         img_path = os.path.join(parent_path, 'img')
    #         print(img_path)
    #         current_time = time.strftime('%Y-%m-%d-%H%I%M', time.localtime(time.time()))
    #         file_name = os.path.join(img_path, current_time + ".png")
    #
    #         self.get_screenshot_file(file_name)
    #
    #         return False
    #




if __name__ == '__main__':
    driver = webdriver.Chrome()
    ip = IndexPage(driver)
    ip.app_send()

    ip.center()