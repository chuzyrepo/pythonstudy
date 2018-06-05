#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#ord()
print(ord('A'))
#chr()
print(chr(65))
print(chr(25991))
#已知字符串编码情况下
print('\u4e2d\u6587')
#字符串转换为字节encode()
a = 'ABC'.encode('ascii')
print(a)
b = '中文'.encode('utf-8')
print(b)
#字节码转换为字符串decode()
c = b'ABC'.decode('ascii')
print(c)
d = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(d)
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
d = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(d)
#要计算str包含多少个字符，可以用len()函数
print(len('ABC'))
print(len('中文'))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))
