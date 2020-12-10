#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: page.py
@time: 2020/11/17 13:25
@desc:
'''

from  selenium import webdriver
from  selenium.webdriver.common.by import  By

from Base.basePage import *

from time import sleep

class SearchPage(BasePage):

    input_id = (By.ID,'kw')
    click_id = (By.ID,'su')

    '''
    操作页面的元素 ,输入内容
    '''
    def input_text(self,text):

        self.clamator_element(self.input_id).send_keys(text)


    '''
    点击操作 
    '''
    def click(self):

        self.clamator_element(self.click_id).click()


    '''
    自测验证
    '''
    def search(self):

        text = 'python'
        sp.open()
        sp.input_text(text)
        sp.click()
        sp.quit()


if __name__ == '__main__':
    url = 'http://www.baidu.com'

    driver = webdriver.Chrome()
    sp = SearchPage(driver, url)
    sp.open()
    sleep(5)

    sp.input_text('python')
    sp.click()
    sp.quit()


