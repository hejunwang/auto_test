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


from email.mime.text import MIMEText

from configparser import ConfigParser
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os

class sendEmail:

    def __init__(self):
        # 读配置文件
        conf =ConfigParser()
        conf.read('../config/email.ini')
        smtp_server = conf.get('DEFAULT','MAIL_HOST')
        print(smtp_server)

        # 第三方配置文件
        self.MAIL_HOST=conf.get('DEFAULT','MAIL_HOST')      #服务器设置
        self.MAIL_USER=conf.get('DEFAULT','MAIL_USER')         #用户名
        self.MAIL_PASS = conf.get('DEFAULT','MAIL_PASS')   #口令

        self.MAIL_SENDER=conf.get('DEFAULT','MAIL_SENDER')
        self.MAIL_RECEIVER =conf.get('DEFAULT','MAIL_RECEIVER')

        print("MAIL_HOST:{}".format(self.MAIL_HOST))
        print("MAIL_USER:{}".format(self.MAIL_USER))
        print("MAIL_PASS:{}".format(self.MAIL_PASS))
        print("MAIL_SENDER:{}".format(self.MAIL_SENDER))
        print("MAIL_RECEIVER:{}".format(self.MAIL_RECEIVER))




    def last_report(self,report_path):
        '''
         #获取最新的测试报告
        :param report_path:
        :return: file_new
        '''
        lists = os.listdir(report_path)
        print('lists-->{}'.format(lists))

        lists.sort(key=lambda fn:os.path.getmtime(report_path+'\\'+fn))
        file_new = os.path.join(report_path,lists[-1])
        return file_new


    def send_email(self):
        '''
        三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        :return:
        '''
        message = MIMEMultipart()

       # 发送者
        message['From'] = self.MAIL_SENDER
        # 接收者
        message['To'] = self.MAIL_RECEIVER

        # 邮件主题
        subject = 'POM设计模式,关键字驱动设计模式,ddt数据驱动,yaml,requests   --report'
        message['Subject'] = Header(subject, 'utf-8')


        # 邮件文本内容
        message.attach(MIMEText('Python api 接口 - sendemail 邮件发送...smtplib.report ', 'plain', 'utf-8'))

        parent_path = os.path.dirname(os.getcwd())  # 将当前目录传入得到当前目录的父目录
        report_path = os.path.join(parent_path, 'Report')
        lastfile = self.last_report(report_path)
        print('lastfile:--->{}'.format(lastfile))

        # 添加附件
        att1 = MIMEText(open(lastfile,'rb').read(),'base64','utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="report_file.html"'
        message.attach(att1)


        # 发送邮件
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.MAIL_HOST, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.MAIL_USER, self.MAIL_PASS)
            smtpObj.sendmail(self.MAIL_SENDER, self.MAIL_RECEIVER, message.as_string())
            print("Email send Success")
            smtpObj.quit()
        except smtplib.SMTPException as e:
            print('"Error: send email failed :{}'.format(e))
            raise e




if __name__ == '__main__':
    se = sendEmail()
    se.send_email()


