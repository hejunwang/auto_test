#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 10:54
# @Author  : toby
# @Site    : 
# @File    : test1.py
# @Software: PyCharm



import pytest

class Test_abc:

    def setup_class(self):
        print('-------------setup class')


    def teardown_class(self):
        print('-------------teardown class')


    def test_1(self):
        assert 1
        print('------------test_1')

    #  pytest 中使用 pytest.raises() 进行异常捕获：
    def test_raise(self):
        print('----------raise')
        assert 1

    def test_b(self):
        print('---------test-b')

if __name__ == '__main__':
    pytest.main(['test1.py' ,'--html=report.html','-s','-v','-q'])

