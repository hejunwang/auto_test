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


class sendEmail:

    def __init__(self):
        # 读配置文件
        conf =ConfigParser()
        conf.read('../config/email.ini')
        smtp_server = conf.get('DEFAULT','MAIL_HOST')
        print(smtp_server)

        #     第三方配置文件
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


    def send_email(self):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEMultipart()
        message['From'] = Header("sender", 'utf-8')  # 发送者
        message['To'] = Header("receiver", 'utf-8')  # 接收者

        subject = '报告 邮件'
        message['Subject'] = Header(subject, 'utf-8')

        message.attach(MIMEText('Python 邮件发送...smtplib.'
                                , 'plain', 'utf-8'))

        # message['From'] ='hejunwang01@126.com'
        # message['To'] = 'hejunwang02@126.com'

        # 附件
        # att1 = MIMEText(open('../testcast/mytest.py','rb').read(),'base64','utf-8')
        #
        # att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        # message.attach(att1)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.MAIL_HOST, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.MAIL_USER, self.MAIL_PASS)
            smtpObj.sendmail(self.MAIL_SENDER, self.MAIL_RECEIVER, message.as_string())
            print("邮件发送成功")
            smtpObj.quit()
        except smtplib.SMTPException as e:
            print('"Error: 无法发送邮件"')
            raise e




if __name__ == '__main__':
    se = sendEmail()
    se.send_email()


