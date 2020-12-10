#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: base.py
@time: 2020/11/17 13:18
@desc:
'''

from time import sleep
from selenium import webdriver

class BasePage:
    '''
    init 初始化
    '''
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)


    '''
    打开
    '''
    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    '''
    元素获取
    '''
    def clamator_element(self,clamator_id):
         return self.driver.find_element(*clamator_id)

    '''
    关闭
    '''
    def quit(self):
        self.driver.quit()

    "输入文本"
    def input_(self,clamator_id,text):
        self.clamator_element(clamator_id).send_keys(text)


    "等待"
    def wait_(self,time_):
        sleep(time_)



    "点击"
    def click_(self,clamator_id):
        self.clamator_element(clamator_id).click()


    "ifram_switch"
    def switch_to_iframe(self,clamator_id):
        iframe = self.clamator_element(clamator_id)
        self.driver.switch_to_frame(iframe)


    "获取当前地址"
    def get_currenturl(self):
        return self.driver.current_url