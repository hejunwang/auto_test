#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: loginpage.py
@time: 2020/12/10 9:44
@desc:
'''

from Base.basePage import BasePage
from selenium.webdriver.common.by import By

from selenium import webdriver

class LoginPage(BasePage):

    '''
    输入地址
    账户
    密码
    点击登录
    '''

    url = 'http://126.com'
    btn = (By.ID, 'dologin')
    user = (By.NAME, 'email')
    passwd = (By.NAME, 'password')
    toiframe = (By.XPATH, '//div[@id="loginDiv"]/iframe')

    # 登录
    def login(self,user,passwd):

        # 打开网页
        self.open(self.url)
        # 切换到iframe中
        self.switch_to_iframe(self.toiframe)
        self.wait_(2)
        # 输入账户和密码
        self.input_(self.user,user)
        self.input_(self.passwd,passwd)

        self.click_(self.btn)
        self.wait_(2)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = 'hejunwang02'
    passwd = 'hejunw123'
    lp = LoginPage(driver)
    lp.login(user,passwd)







