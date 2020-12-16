'''
Author       : Wang.HH
Date         : 2020-11-18 13:42:41
LastEditTime : 2020-12-15 08:36:06
LastEditors  : Wang.HH
Description  : your description
FilePath     : /My-VUE-Python/wewew/hgteaysg.py
'''

if __name__ == '__main__':
    print("程序自身运行")
else:
    print("模块被调用")


def print_func(par):
    print("AH! ", par)
    return


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print('end-end')


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
