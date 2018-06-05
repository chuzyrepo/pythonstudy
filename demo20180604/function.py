#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math #import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
#基本上所有的高级语言都支持函数，Python也不例外。Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用。
#调用函数
#Python内置了很多有用的函数，我们可以直接调用
#要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
#也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
print(abs(100))
print(abs(-10))
#max函数max()可以接收任意多个参数，并返回最大的那个：
print(max(1,20,6,8,9,50))
#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print(int('100')+100)
print(float('100')+100)
print(str(100)+'100')
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1))
# hex()将整数转为十六进制数
print(hex(45))
# 定义函数
# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(a):
    if a>= 0:
        return a
    else:
        return -a
print(my_abs(-9))
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
# 在Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下：
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# pass还可以用在其他语句里，比如：


age = 10
if age>10:
    pass


# 优化my_abs()


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


my_abs(1)

#返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x,y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#  所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


# 函数的参数
# 1.位置参数   与java相似，此处不再赘述
# 2.默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 此处的n即为默认参数，默认等于2
# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
#函数的参数
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
# 位置参数
# 我们先写一个计算x2的函数：


def power(x):
    return x * x
# 对于power(x)函数，参数x就是一个位置参数。
# 当我们调用power函数时，必须传入有且仅有的一个参数x：
# >>> power(5)
# 25
# >>> power(15)
# 225
# 现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。
# 你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 对于这个修改后的power(x, n)函数，可以计算任意n次方：
# >>> power(5, 2)
# 25
# >>> power(5, 3)
# 125
# 修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
# 默认参数
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
# >>> power(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: power() missing 1 required positional argument: 'n'
# Python的错误信息很明确：调用函数power()缺少了一个位置参数n。
# 这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 这样，当我们调用power(5)时，相当于调用power(5, 2)：
# >>> power(5)
# 25
# >>> power(5, 2)
# 25
# 而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。
# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# 举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数：


def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
# 这样，调用enroll()函数只需要传入两个参数：

# >>> enroll('Sarah', 'F')
# name: Sarah
# gender: F
# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。

# 我们可以把年龄和城市设为默认参数：


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：

# >>> enroll('Sarah', 'F')
# name: Sarah
# gender: F
# age: 6
# city: Beijing
# 只有与默认参数不符的学生才需要提供额外的信息：


enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
# 可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，
# 除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。
# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
# 先定义一个函数，传入一个list，添加一个END再返回：


def add_end(L=[]):
    L.append('END')
    return L
# 当你使用默认参数调用时，一开始结果也是对的：
# >>> add_end()
# ['END']
# 但是，再次调用add_end()时，结果就不对了：
# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 优化如下：


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，
# 对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 但是调用的时候，需要先组装出一个list或tuple：还是太麻烦


a = calc([1, 2, 3])
print(a)
# 利用可变参数就显得简单了


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 与上面相比就多了一个*，但是在调用时就方便很多了


a = calc(1, 2, 3)
print(a)
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
calc(*nums)
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：


person('Michael', 30)
# 也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# 当然，上面复杂的调用可以用简化的写法：
person('Jack', 24, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
#
# 仍以person()函数为例，我们希望检查是否有city和job参数：


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 但是调用者仍可以传入不受限制的关键字参数：
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：


def person(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#
# 调用方式如下：
person('Jack', 24, city='Beijing', job='Engineer')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person('Jack', 24, job='Engineer')
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
#########################################################
###########################################################
# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
