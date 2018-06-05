#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
#获取list长度len()
print(len(classmates))
#用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
#以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-2])
#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('hanmeimei')
#也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1,'lilei')
#要删除list末尾的元素，用pop()方法：
classmates.pop()
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'ddddd'
#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
#list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
##############################################################
##############################################################
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，
# 但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1, 2)
#如果要定义一个空的tuple，可以写成()：
t = ()
#当tuple只有一个元素时，需加逗号来消除歧义
t = (1,)#如果不加逗号，此时会被当成数学中的小括号 打印结果为1
#“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
print(t)
