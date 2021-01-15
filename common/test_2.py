#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 18:36
# @Author  : toby
# @Site    : 
# @File    : test_2.py
# @Software: PyCharm


# 99乘法表
# 冒泡
#阶乘
# m幂次方
# 斐波那契数列

# 99乘法表
def chengfb():
    for i in range(1,10):

        for j in range(1,i+1):

            print("%d*%d=%d  " %(i,j,i*j),end='')

            if i==j:
                print('\n')

# 冒泡
def maopao(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1,n-i-1):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print('冒泡后的数组')
    print(arr)

#  n m   5*4*3*2*1  #阶乘
def jiec(n):
    if n ==1:
        return 1
    else:
        print('n: %d' %n)
        return  n*jiec(n-1)


# m幂次方  5**3
def micf(n,m):
    if m ==1:
        return  n
    else:
        print('n:%d' %n)
        return n*micf(n,m-1)


# 斐波那契数列   1,1,2,3,5,8,13  ,100以内
def feibnaq(m):
    a = 0
    b = 1
    fbn=[]
    while b<m:
        a,b = b,a+b
        fbn.append(b)
    print('斐波那契数列:')
    print(fbn)

# 素数（prime number）又称质数 除了1和它本身以外不再被其他的除数整除。
def sushu(n,m):
    ss=[]
    for num in range(n,m+1):

        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                ss.append(num)
    
    print('素数:')
    print(ss)


if __name__ == '__main__':
    chengfb()
    arr = [1,4,3,2,5]
    maopao(arr)
    print(jiec(5))
    print(micf(5,3))
    feibnaq(30)
    sushu(10,100)


