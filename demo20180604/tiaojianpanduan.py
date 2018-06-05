#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = 20
if age<18:
    print('未成年！')
elif age>18:
    print('你是个成年人啦！')
#if判断条件还可以简写，比如写：
x = 12 #只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if x:
    print("dadada")


s = input('birth: ')
birth = int(s)#将str转为整数
if birth < 2000:
    print('00前')
else:
    print('00后')


#循环
#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['zhangsan','lisi','wangwu']
for name in names:
    print(name)
#计算1到100的和
#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
nums = list(range(101))
sum = 0
for num in nums:
    sum += num
print(sum)

#while循环
#只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
num = 99
while num>0:
    sum+=num
    num -=2
print(sum)

#break
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)