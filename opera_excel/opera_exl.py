#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: opera_exl.py
@time: 2020/11/13 13:44
@desc:
'''


import openpyxl

import os

class Read_exl:

    def __init__(self,file_path):

        self.wb = openpyxl.load_workbook(file_path)
        self.sheet1_name = self.wb.get_sheet_names()[0]
        print(self.wb)
        print(self.sheet1_name)






    def readExcel(self):

        pass


if __name__ == '__main__':
    file_path = os.getcwd()
    print(file_path)
    Read_exl(r'../data/data.xlsx')