#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
print(d)
#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Adam'] = 88
print(d) #如果key不存在，dict就会报错：
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
a = 'Thomas' in d
print(a)
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
b = d.get('Thomas')
print(b)
b = d.get('Thomas',-1)
print(b)
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Michael')
print(d)
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
#
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：


