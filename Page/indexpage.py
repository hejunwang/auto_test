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


    def index_all(self):
        self.app_send()
        self.wait_(2)
        self.center()






if __name__ == '__main__':
    driver = webdriver.Chrome()
    ip = IndexPage(driver)
    ip.app_send()

    ip.center()