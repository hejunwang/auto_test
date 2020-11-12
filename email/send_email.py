#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: send_email.py
@time: 2020/11/12 21:02
@desc:
'''

import smtpd
from email.mime.text import MIMEText

class sendEmail:

    def sendemail(self):

        smtp_server = "hejunwang02@126.com"
        smtp_port = 445
        smtp_name = "xxxx"
        smtp_pwd = "xxxx"

