# -*- coding: UTF-8 -*-
import hgteaysg
import math
import cmath
import random
# import sys
input("按下enter键退出，其他任意键显示...\n")
print('ok!')
'''
13212312
'''
a, b = 67, '7'
a, b = b, a
print(a, b)
s = 'abcdefg'
print(s[-6:-2])
d = ['1', '2', '3', '4', '5']
print(d[1:4])
print(d[1:4:2])
print(d[1:4:2] * 2)
print(d[1:4] + d[1:4:2])
e = ('1', '2', 3, 4, 5)  # 元组，相当于只读列表，元组不允许更新，列表可以更新，其他功能与列表相同
'''
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dictionary = {}
dictionary['one'] = "this is one!"
dictionary[999] = "this is two!"
print(dictionary)
print(dictionary[999])
f, g = list(dictionary.keys()), list(dictionary.values())
# python3 dict.keys()不再直接返回list类型了，也不支持索引，解决办法是在外层套一个list()就可以了
print(f, g)  # 输出字典所有键,输出字典所有值
print(type(f))
print(type(a))
print(type(int(a)), type(a), int(a))
print(tuple(f[0]))
print(type(b), chr(b))  # 将一个整数转换为对应的ASCII码字符
a, b, c = 21, 10, 0
c = a // b
print(c)  # 取整除，返回商的部分（向下取整）
c = a / b
print(c)
c = b**a
print(c)  # 返回x的y次幂
a = 60
b = 13
# 位运算
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a >> 4)
if a and b:
    print("a和b都是true")
else:
    print("a和b有一个不为true")
if a or b:
    print("a和b都是true")
else:
    print("a和b有均不为true")
if not a:
    print("a为0或者假")
else:
    print("a为真")
_list = [1, 2, 3, 4, 5]
_a = 10
_b = 11
if (_a in _list):
    print("变量_a在给定的列表_list中")
else:
    print("变量_a不在给定的列表_list中")
if (_b not in _list):
    print("变量_b不在给定的列表_list中")
else:
    print("变量_b在给定的列表_list中")
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
a = [1, 2, 3]
b = a
print(b is a)
print(b == a)
b = a[:]
print(b is a)
print(b == a)
a = 1
while a < 7:
    if (a % 2 == 0):
        print(a, "is even")
    else:
        print(a, "is odd")
    a += 1
numbers = [12, 37, 5, 32, 5, 86]
even = []
odd = []
while len(numbers) > 10:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
else:
    print("请检查数组！")
print("even:", even, "odd:", odd)
hjhjhj = ['banana', 'apple', 'mango']
for fruit in hjhjhj:
    print("当前水果:", fruit)
print(range(len(hjhjhj)))
print('再见')
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d等于%d*%d" % (num, i, j))
            break
    else:
        print(num, "是一个质数")
i = 2
while i < 100:
    j = 2
    while j < i / j:
        if not (i % j):
            break
        j += 1
    if (j > i / j):
        print(i, "是素数")
    i += 1


def testfun(a):
    pass


print("float:", float(i))
del i
print(dir(math))
print(dir(cmath))
print(cmath.sqrt(-7))
print(cmath.sqrt(7))
print(cmath.exp(100))
print(random.choice(range(10)))
print(math.e)
print(random.randint(0, 10))
random.seed(10)
print(random.random(), random.seed(10), random.random())
a, b = 2, 2
print((a > b) - (b > a))
print(max(range(10)))
print(random.randrange(2, 100, 2))
print("123213\r")
print(r"\n")
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)
print(f'13123213213213---123{errHTML}')
x = 1
print(f'{x+1=}\n')
str_a = 's\tis\tstr_a!'
print(str_a.capitalize())
print(str_a.center(100, '-'))
print(str_a.count('is'))
str_b = '哈哈哈'
str_utf8 = str_b.encode('UTF-8')
str_gbk = str_b.encode('GBK')
print(str_utf8, str_gbk)
print('解码utf-8：', str_utf8.decode('UTF-8', 'strict'))
print('解码gbk：', str_gbk.decode('GBK', 'strict'))
print(str_a.expandtabs(2))
print(str_a.expandtabs(5))
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz',
                                 b'!@#$%^&*()_+1234567890-=[]')
print(b'wang hao hao'.translate(bytes_tabtrans))
language = ['French', 'English', 'German']
language_tuple = ('Spanish', 'Protuguese')
language_set = {('2', ): '1', '1': '2', '4': '3', '3': '4', '5': '5'}
language.extend(language_tuple)
print('新列表1：', language)
language.extend(language_set)
print('新列表2：', language)
print(language_set[('2', )])
seq = ('name', 'age', 'sex')
dictionary_fromkeys = dict.fromkeys(seq, 10)
print(dictionary_fromkeys)
fruit = {'apple', 'orange', 'apple', 'orange', 'banana', 'pear'}
print(fruit)
print('apple' in fruit)
a = set('abtrsabsw')
b = set('atgopuytqn')
print(a, b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
a.add('123')
print(a)
a.update({1, 2, 3})
print(a)
a.remove('123')
print(a)
a.discard('bbb')
print(a)
print(a.pop())
a, b = 0, 1
while b < 10:
    print(b, end=',\n')
    a, b = b, a + b
num = int(input('请输入一个正整数：'))
if num % 2 == 0:
    print(f'{num}是双数！')
else:
    print(f'{num}是单数！')
list_test = [1, 2, 3, 4]
it = iter(list_test)
for x in it:
    print(x)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print('press ctrl+c!')
#         sys.exit()
# for rr in it:
#     print(rr, end=" ")


def fibonacc(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


# f = fibonacc(10)
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = Mynumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))


def change(a):
    print(id(a))
    a = 10
    print(id(a))


a = 1
print(id(a))
change(a)


def mychange(list):
    list.append([1, 2, 3, 4])
    print('函数内取值：', list)
    return


mylist = [10, 20, 30]
mychange(mylist)
print('函数外取值：', mylist)

vec = [2, 4, 6]
print("列表推导式1：", [3 * x for x in vec])
print("列表推导式2：", [[2 * x, x**2] for x in vec])


def deboule(num):
    return num * 2


veb = ['     b', 'a      b', 'b n', 'n             ']
print("列表推导式3：", [deboule(x) for x in vec if x > 2])
print("列表推导式4：", [x.strip() for x in veb])

a, b = set('fasttgfsd'), set('asdasdasdhsadk')
c = [1, 2, 3, 4, 5]
d = set([1, 1, 1, 2, 3, 3, 4])
print(a, b)
print(c[1:2])
print([x for x in d])
print({x for x in d})
print(a | b)
print(a & b)
print(a ^ b)
print({x for x in 'abracadabra' if x not in 'abcd'})

vdsa = dict([('sape', 1), ('ggg', 2), ('jjj', 3)])
print({k: v**2 for k, v in vdsa.items()})

hgteaysg.print_func('jjjj')
