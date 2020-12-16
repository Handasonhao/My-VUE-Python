'''
Author       : Wang.HH
Date         : 2020-09-17 15:41:00
LastEditTime : 2020-12-15 14:56:02
LastEditors  : Wang.HH
Description  : your description
FilePath     : /My-VUE-Python/wewew/3.py
'''

import xlrd


def readExcel():
    workbook = xlrd.open_workbook("C:/Users/王浩浩/Desktop/API数据整理.xls")
    print(workbook.sheet_names())
    sheet = workbook.sheet_by_index(0)
    print(sheet.nrows)
    for x in range(1, 11):
        rows = sheet.row_values(x)
        print(rows)


if __name__ == '__main__':
    readExcel()
