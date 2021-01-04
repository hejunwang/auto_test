#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: uiauto2.py
@time: 2020/12/30 17:37
@desc:
'''

import uiautomator2 as ut

import threading
from time import sleep

# 单例模式
class Singleton():

    _instance_lock = threading.Lock
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls,'_instance'):
            with Singleton._instance_lock:
                if not hasattr(cls,'_instance'):
                    Singleton._instance = super().__new__(cls)

            return Singleton._instance



class UiautoMator():

    # 初始化
    def __init__(self,addr):
        self.driver = ut.connect(addr=addr)
        self.driver.implicitly_wait(10)



    # 启动app
    def startapp(self,package_name,activity):
        self.driver.app_start(package_name,activity)

    # 点击
    def click(self,text):
        self.driver(text =text).click()

    # 长按
    def long_click(self,text):
        self.driver(text =text).long_click()

    # 发送文本
    def send_keys(self,text,value):
        self.driver(text =text).send_keys(value)

    # 强制等待
    def wait(self,time_):
        sleep(time_)


    # 点击home
    def press_home(self):
        self.driver.press('home')


    #
    def press_back(self):
        self.driver.press('back')








if __name__ == '__main__':

    # 连接设备
    ua = UiautoMator('emulator-5554')
    print(ua.driver.device_info)

    # 要启动的app
    # "package": "com.lilithgames.afk.aligames",
    # "activity": "cn.gundam.sdk.shell.activity.ProxyActivity"
    ua.startapp("com.lilithgames.afk.aligames","cn.gundam.sdk.shell.activity.ProxyActivity")
    # ua.startapp("com.android.browser","com.android.browser.BrowserActivity")
    print('启动app')
    ua.wait(20)
    ua.press_home()
