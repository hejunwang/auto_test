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
import copy
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

# 乘法口诀
def chengfakoujue():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d  " %(i,j,i*j),end='')
            if j==i:
                print('\n')


#冒泡排序,首先遍历数组 ,然后一个一个进行的比较 ,如果前面的一个大于后面的,进行前后调换排序
def bubbleSort(arr):
    n = len(arr)
#     遍历数组
    for i in range(n):

        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]       #交换

    for i in arr:
        print('%d' %i ,end='')

    print(arr)


# 阶乘  5*4*3*2*1
def digui(n):
    if n ==1 :
        return  1
    else:
        return n*digui(n-1)

# 幂次方  5*5*5*5  n 底数 ,m 幂次数
def micifang(n,m):
    if m==0:
        return 1
    else:
        return n*micifang(1,n-1)


# 斐波那契数列  1 ,1,2,3,5,8  ,,  100以内的
def feibo(m):
    a =0
    b =1
    while b < m:
        print(b,end=',')
        a ,b = b,a+b


# 素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。
def zhishu(n,m):
    # 遍历这个区间
    for num in range(n,m+1):
        if num>1:
            for i in range(2,num):    # 从2 开始 ,到这个数之间进行整除
                if num%i==0:
                    break
            else:
                print('sushu: %d' %num)


# 水仙花  问题1：打印出100-999所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

def  shuixianhua():
    sxh =[]
    for i in range(100,1000):
        s = 0
        m = list(str(i))
        for j  in m:
            s += int(j)**len(m)

        if i ==s:
            sxh.append(i)
    print(sxh)

    sxh2=[]
    for i in range(1000,10001):
        s = 0
        m = list(str(i))
        for j  in m:
            s += int(j)**len(m)

        if i ==s:
            sxh2.append(i)

    print('sxh2:')
    print(sxh2)


# 装饰器, 参数是函数 ,不会改变原来函数的功能 ,   闭包函数使用的是外部函数中的变量,延长了变量的声明周期
def count_time(fun):
    def wrapper(*args):
        print("1111111111111")
        res= fun(args)
        print("22222222")
        return res
    return wrapper

@count_time
def function_1(text):
    print('this is %s' %text)




def string_opera():
    str = " this is a title "
    print('所有首字母大写:'+str.title())
    print('第一个:'+str[0])
    print('从第二个字母开始:'+str[2:])
    print('最后一个字符:'+str[-1])
    print("倒叙:"+str[::-1])
    print("首字母大写:"+str.capitalize())
    print('翻转大小写:'+str.swapcase())
    print('是否是数字:')
    print(str.isdigit())
    print('删除右边的空格:'+str.rstrip())
    print('删除zuo边的空格:'+str.lstrip())

    if 's' in str:
        print("s in str 中 ")


def list_opera():
    array=[1,3,5,3,4]
    array2=[1,3,5,3,4]
    array.append(9)
    print(array)
    array.extend(array2)
    print(array)

    print("反向列表")
    array2.reverse()
    print(array2)

    print('排序')
    array2.sort()
    print(array2)

    print('tuple')
    str = '123sdfsdf'
    print(tuple(str))

    print('迭代,生成器')

    it = iter(array)
    for x in it:
        print(x,end='')



def dict1():
    d = {"a":['Google', 'www.google.com'], 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
    for key,value in d.items():
        print(key,value)
    print(str(d))
    print(type(str(d)))

#     浅拷贝
    d1 = d.copy()
    print(d1)

    # 深拷贝
    d2 = copy.deepcopy(d)
    d['a'].append('www.baidu.com')
    print('修改d')
    print(d)
    print('d1是否修改 ,如果修改 就是浅拷贝')
    print(d1)

    print('深拷贝未修改')
    print(d2)




total = 0  # 这是一个全局变量
# 可写函数说明
def sum_(arg1, arg2):
    # 返回2个参数的和."
    # total = arg1 + arg2  # total在这里是局部变量.
    global  total
    total = total+1
    print("函数内是局部变量 : ", total)
    return total

print(total)






if __name__ == '__main__':
    # res = hex_to_dec('0xa')
    # print(res)

    # res = jiema()
    # print(res)

    # des_ret = descover()
    # print(des_ret)

    # chengfakoujue()

    arr = [2,5,32,7,1,21,4,6]
    bubbleSort(arr)

    function_1('world')
    string_opera()

    list_opera()

    print(digui(4))

    feibo(100)

    zhishu(3,50)

    shuixianhua()

    dict1()

    # 调用sum函数
    print(sum_(10, 20))

    feibonaqi(100)

    while True :
        try:
            print(next(feibonaqi(100)),end='')
        except StopIteration:
            import sys
            sys.exit()


