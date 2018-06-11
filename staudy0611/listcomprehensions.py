import os
# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
l1 = list(range(1, 11))
print(l1)
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for i in range(1, 11):
    L.append(i*i)
print(L)
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
l2 = [x * x for x in range(1, 11)]
print(l2)
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
#
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l3)
# 还可以使用两层循环，可以生成全排列：
l4 = [m + n for m in 'ABCDEFG' for n in 'abcdefg']
l5 = [m + n for m in 'ABC' for n in 'XYZ']
print(l4)
print(l5)
# 三层和三层以上的循环就很少用到了。
#
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
l6 = [d for d in os.listdir('.')]
print(l6)
# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
# 因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
l7 = [k + '=' + v for k, v in d.items()]
print(l7)

# 把一个list中所有的字符串变成小写：
d1 = ['A', 'B', 'C', 'D', 'E']
d2 = [n.lower() for n in d1]
print(d2)

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# 使用内建的isinstance函数可以判断一个变量是不是字符串：
a = isinstance('ava', str)
b = isinstance(123, str)
print(a)
print(b)
