#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: ci_jenkins_py.py
@time: 2020/12/16 17:27
@desc:
'''

import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='123456')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
