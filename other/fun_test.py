#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: garner
@file: fun_test.py
@time: 2020/12/28 17:05
@desc:
'''

# 十六进制的转换 10进制
def hex_to_dec(*args):
    print(list(args))
    s= []
    for i in args:
        s.append(int(i,16))
    return s

#解码   YUANzhi1987  -->zvbo9441987
def jiema():
    s = input("请输入密码:")
    print(s)
    if len(s)>60:
        print('超出了长度')
    else:
        res = []
        for i in s :
            if i.isalpha():          #字符串.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。

                if i.isupper():
                    if i is "Z":   #如果是大写的Z ,下一个字母就是大写的A
                        res.append(chr(ord('A'.lower())))
                    else:
                        res.append(chr(ord(i.lower())+1) )            #ord(x )  将一个字符转换为它的整数值
                else:
                    if i is 'z':
                        res.append(chr(ord('a')))
                    else:
                        res.append(   chr(  ord(i) + 1  )   )

            else:
                # 代表是数字
                res.append(i)
        return  ''.join(res)



# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# 保证输入的整数最后一位不是0。输入一个int型整数,按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

def descover():
    s = input("输入一串数字 ,最后一位不能是0 >>>\n ")
    ls =list(s)[::-1]
    l2 = list(set(ls))
    print(l2)

    l2.sort(key=ls.index)
    print(l2)

    return int(''.join(l2))







if __name__ == '__main__':
    # res = hex_to_dec('0xa','0xf','0xAA')
    # print(res)
    # res = hex_to_dec('0xa')
    # print(res)
    #
    # res = jiema()
    # print(res)

    des_ret = descover()
    print(des_ret)


