# python高级特性 切片
# 使用循环取一个list的前n个元素
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(6):
    print(list1[i])
# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
print(list1[0:6])  # 获取前6个元素，索引0-5不包括6
# 如果索引由0开始，0可以省略
print(list1[:6])
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(list1[-1:])
print(list1[-2:-1])
# 每两个取一个
print(list1[:9:3])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(list1[:])
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple1[:9])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
str = 'abcdefghijklmn'
print(str[:9])