#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: sqloperate.py
@time: 2020/12/18 11:28
@desc:
'''

import pymysql

class MySql_DB:

    def __init__(self):
        self.db = pymysql.connect('ip','user','pwd','db')
        self.coursor = self.db.cursor()


    def select_db(self,sqlstring):
        pass
        sqlstring = 'select * from userinfo'
        self.coursor.execute(sqlstring)
        dd = self.coursor.fetchall()

    def updata(self):

        sqlstring = 'insert into tablename (id,age) values(1,2) '
        try:
            self.coursor.execute(sqlstring)
            self.db.commit()
        except:
            self.db.rollback()


    def close_db(self):
        self.db.close()


