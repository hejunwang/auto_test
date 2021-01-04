#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: appiumcase.py
@time: 2020/12/30 11:42
@desc:
'''

from appium import webdriver

des={
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "HMA-AL00",
    "appPackage": "com.android.browser",
    "appActivity": ".BrowserActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',desired_capabilities=des)
driver.find_element_by_xpath('')

